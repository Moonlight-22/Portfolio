import { FaMoon, FaSun } from 'react-icons/fa'
import useTheme from '../../hooks/useTheme'

export default function ThemeToggle() {
  const { theme, setTheme } = useTheme()
  const isDark = theme === 'dark'

  return (
    <button
      type="button"
      onClick={() => setTheme(isDark ? 'light' : 'dark')}
      className="rounded-full border border-slate-300/60 bg-white/60 p-2 text-slate-700 transition hover:scale-105 dark:border-slate-700 dark:bg-slate-900/70 dark:text-slate-100"
      aria-label={`Switch to ${isDark ? 'light' : 'dark'} mode`}
    >
      {isDark ? <FaSun /> : <FaMoon />}
    </button>
  )
}
