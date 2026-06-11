import React, { useEffect, useRef } from 'react'

export default function MindMapCanvas() {
  const canvasRef = useRef(null)
  const animRef = useRef(null)
  const nodeIntervalRef = useRef(null)
  const nodesRef = useRef([])
  const edgesRef = useRef([])
  const countRef = useRef(0)

  useEffect(() => {
    const canvas = canvasRef.current
    if (!canvas) return

    const resize = () => {
      canvas.width = canvas.offsetWidth
      canvas.height = canvas.offsetHeight
    }
    resize()
    window.addEventListener('resize', resize)

    // Seed center node
    nodesRef.current = [{
      x: canvas.width / 2, y: canvas.height / 2,
      r: 7, alpha: 0, color: '#F97316'
    }]
    edgesRef.current = []
    countRef.current = 0

    const addNode = () => {
      if (countRef.current > 25) return
      countRef.current++
      const parent = nodesRef.current[Math.floor(Math.random() * Math.min(nodesRef.current.length, 6))]
      const angle = Math.random() * Math.PI * 2
      const dist = 40 + Math.random() * 90
      const nx = Math.max(10, Math.min(canvas.width - 10, parent.x + Math.cos(angle) * dist))
      const ny = Math.max(10, Math.min(canvas.height - 10, parent.y + Math.sin(angle) * dist))
      const colors = ['#F97316', '#FB923C', '#FED7AA', '#EA580C']
      const newNode = { x: nx, y: ny, r: 3 + Math.random() * 4, alpha: 0, color: colors[Math.floor(Math.random() * colors.length)] }
      nodesRef.current.push(newNode)
      edgesRef.current.push({ from: parent, to: newNode, alpha: 0 })
    }

    const draw = () => {
      const ctx = canvas.getContext('2d')
      ctx.clearRect(0, 0, canvas.width, canvas.height)

      edgesRef.current.forEach(e => {
        e.alpha = Math.min(1, e.alpha + 0.04)
        ctx.beginPath()
        ctx.moveTo(e.from.x, e.from.y)
        ctx.lineTo(e.to.x, e.to.y)
        ctx.strokeStyle = `rgba(249,115,22,${e.alpha * 0.28})`
        ctx.lineWidth = 1
        ctx.stroke()
      })

      nodesRef.current.forEach(n => {
        n.alpha = Math.min(1, n.alpha + 0.05)
        const hex = n.color
        const r = parseInt(hex.slice(1, 3), 16)
        const g = parseInt(hex.slice(3, 5), 16)
        const b = parseInt(hex.slice(5, 7), 16)
        ctx.beginPath()
        ctx.arc(n.x, n.y, n.r, 0, Math.PI * 2)
        ctx.fillStyle = `rgba(${r},${g},${b},${n.alpha})`
        ctx.shadowColor = `rgba(${r},${g},${b},0.5)`
        ctx.shadowBlur = 8
        ctx.fill()
        ctx.shadowBlur = 0
      })

      animRef.current = requestAnimationFrame(draw)
    }

    draw()
    nodeIntervalRef.current = setInterval(addNode, 450)

    return () => {
      cancelAnimationFrame(animRef.current)
      clearInterval(nodeIntervalRef.current)
      window.removeEventListener('resize', resize)
    }
  }, [])

  return <canvas ref={canvasRef} className="loader-canvas" />
}
