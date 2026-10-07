import React, { useEffect, useRef } from 'react'

type Props = {
  title: string
  category: string
  level: number
  description?: string
  thumbnail?: string
}

export default function AnimatedModuleCard({ title, category, level, description, thumbnail }: Props) {
  const ref = useRef<HTMLDivElement | null>(null)
  const stateRef = useRef<any>({
    targetScale: 1,
    curScale: 1,
    targetRX: 0,
    curRX: 0,
    targetRY: 0,
    curRY: 0,
    targetTY: 0,
    curTY: 0
  })

  useEffect(() => {
    const node = ref.current
    if (!node) return

    node.style.willChange = 'transform, box-shadow'
    node.style.transformOrigin = 'center'

    function onEnter() {
      stateRef.current.targetScale = 1.045
    }

    function onMove(e: MouseEvent) {
      const el = ref.current
      if (!el) return

      const r = el.getBoundingClientRect()
      const cx = r.left + r.width / 2
      const cy = r.top + r.height / 2
      const dx = (e.clientX - cx) / (r.width / 2)
      const dy = (e.clientY - cy) / (r.height / 2)

      stateRef.current.targetRX = -dy * 8
      stateRef.current.targetRY = dx * 8
      stateRef.current.targetTY = -Math.abs(dy) * 6
    }

    function onLeave() {
      stateRef.current.targetScale = 1
      stateRef.current.targetRX = 0
      stateRef.current.targetRY = 0
      stateRef.current.targetTY = 0
    }

    node.addEventListener('mouseenter', onEnter)
    node.addEventListener('mousemove', onMove)
    node.addEventListener('mouseleave', onLeave)

    let mounted = true
    const ease = 0.18

    function loop() {
      if (!mounted) return

      const el = ref.current
      if (!el) return

      const s = stateRef.current
      s.curScale += (s.targetScale - s.curScale) * ease
      s.curRX += (s.targetRX - s.curRX) * ease
      s.curRY += (s.targetRY - s.curRY) * ease
      s.curTY += (s.targetTY - s.curTY) * ease

      el.style.transform = `perspective(700px) translateY(${s.curTY}px) rotateX(${s.curRX}deg) rotateY(${s.curRY}deg) scale(${s.curScale})`

      const depth = Math.max(6, 10 + (s.curScale - 1) * 80)
      el.style.boxShadow = `0 ${depth}px ${depth * 2}px rgba(0,0,0,0.6)`

      requestAnimationFrame(loop)
    }

    requestAnimationFrame(loop)

    return () => {
      mounted = false
      node.removeEventListener('mouseenter', onEnter)
      node.removeEventListener('mousemove', onMove)
      node.removeEventListener('mouseleave', onLeave)
    }
  }, [])

  return (
    <div ref={ref} className="card-style rounded-lg shadow-sm overflow-hidden flex flex-col h-full bg-[#272727] border border-[#1f1f1f] transition-shadow duration-300">
      <div className="flex-1 flex items-center justify-center bg-black p-2 min-h-[160px]">
        {thumbnail ? (
          <img
            src={thumbnail}
            alt={title}
            className="max-h-40 w-full object-contain"
          />
        ) : (
          <div className="w-full h-full flex items-center justify-center bg-gradient-to-br from-[#06b6d4]/40 to-[#3b82f6]/20">
            <span className="text-gray-500">No Image</span>
          </div>
        )}
      </div>
      <div className="p-4 bg-[#181818]">
        <h3 className="text-lg font-semibold text-white line-clamp-1">{title}</h3>
        <div className="text-sm text-gray-400 my-1">Kategori: {category}</div>
        {description && (
          <p className="text-gray-400 text-sm mb-2 line-clamp-2">{description}</p>
        )}
        <span className="inline-block text-xs text-white px-2 py-1 rounded-md bg-blue-600 font-medium">
          Level {level}
        </span>
      </div>
    </div>
  )
}
