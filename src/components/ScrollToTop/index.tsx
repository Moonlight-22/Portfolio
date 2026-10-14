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
      className="fixed bottom-20 right-5 z-50 rounded-full bg-sky-600 p-2.5 text-sm text-white shadow-lg transition hover:scale-105 hover:bg-sky-500 md:bottom-5 md:p-3 md:text-base"
      aria-label="Scroll to top"
    >
      <FaChevronUp />
    </button>
  )
}
