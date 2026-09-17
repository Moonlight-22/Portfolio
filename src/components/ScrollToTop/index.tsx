import { useEffect, useState } from 'react'
import { FaChevronUp } from 'react-icons/fa'

export default function ScrollToTop() {
  const [visible, setVisible] = useState(false)

  useEffect(() => {
    const onScroll = () => setVisible(window.scrollY > 400)
    window.addEventListener('scroll', onScroll)
    return () => window.removeEventListener('scroll', onScroll)
  }, [])

  if (!visible) return null

  return (
    <button
      type="button"
      onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })}
      className="fixed bottom-5 right-5 z-50 rounded-full bg-violet-600 p-3 text-white shadow-lg transition hover:scale-105 hover:bg-violet-500"
      aria-label="Scroll to top"
    >
      <FaChevronUp />
    </button>
  )
}
