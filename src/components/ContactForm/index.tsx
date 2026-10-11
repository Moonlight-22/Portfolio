import { useEffect, useState, type FormEvent } from 'react'

const emailAddress = 'aungmyatmin984@gmail.com'

export default function ContactForm() {
  const [isOpen, setIsOpen] = useState(false)
  const [name, setName] = useState('')
  const [message, setMessage] = useState('')

  useEffect(() => {
    if (!isOpen) return

    const handleEscape = (event: KeyboardEvent) => {
      if (event.key === 'Escape') {
        setIsOpen(false)
      }
    }

    window.addEventListener('keydown', handleEscape)
    return () => window.removeEventListener('keydown', handleEscape)
  }, [isOpen])

  const handleSubmit = (event: FormEvent) => {
    event.preventDefault()

    const safeName = name.trim() || 'Portfolio Visitor'
    const safeMessage = message.trim()

    const mailtoLink = `mailto:${emailAddress}?subject=${encodeURIComponent(`Portfolio Inquiry from ${safeName}`)}&body=${encodeURIComponent(
      `Name: ${safeName}\n\nMessage:\n${safeMessage}`
    )}`

    window.location.href = mailtoLink
    setName('')
    setMessage('')
    setIsOpen(false)
  }

  return (
    <div className="relative isolate z-10 mx-auto mt-10 w-full max-w-5xl">
      <div className="relative z-20 rounded-[32px] border border-violet-500/20 bg-[radial-gradient(circle_at_top,_rgba(91,33,182,0.28),_rgba(15,23,42,0.96)_30%,_rgba(2,6,23,1)_100%)] p-5 shadow-[0_25px_90px_rgba(2,6,23,0.9)] transition-all duration-300 ease-out hover:-translate-y-1 hover:shadow-[0_35px_120px_rgba(76,29,149,0.38)] md:p-8">
        <div className="flex flex-col gap-5 md:flex-row md:items-center md:justify-between">
          <p className="max-w-xl text-base leading-relaxed text-slate-200 md:text-lg">
            I’m open to project discussions, collaborations, and business opportunities.
          </p>

          <button
            type="button"
            onClick={() => setIsOpen(true)}
            className="relative z-30 inline-flex w-fit cursor-pointer items-center justify-center rounded-full bg-violet-600 px-6 py-3 text-base font-bold text-white shadow-[0_0_14px_rgba(168,85,247,0.22)] transition-all duration-200 ease-out hover:-translate-y-0.5 hover:bg-violet-500 hover:shadow-[0_0_18px_rgba(168,85,247,0.36)] focus:outline-none focus:ring-2 focus:ring-violet-400/60"
          >
            Send Message
          </button>
        </div>
      </div>

      {isOpen ? (
        <div className="fixed inset-0 z-[100] flex items-center justify-center bg-slate-950/70 p-4 backdrop-blur-sm">
          <div className="relative z-[101] w-full max-w-[720px] rounded-[30px] border border-violet-500/20 bg-[#0b1120]/95 p-5 shadow-[0_35px_120px_rgba(2,6,23,1)] transition-all duration-300 ease-out animate-[fadeIn_0.2s_ease-out] md:p-7">
            <div className="mb-6 flex items-center justify-between gap-4">
              <h3 className="text-2xl font-semibold tracking-tight text-white md:text-3xl">Send a message</h3>
              <button
                type="button"
                onClick={() => setIsOpen(false)}
                className="flex h-10 w-10 items-center justify-center rounded-full text-2xl text-slate-300 transition hover:bg-slate-800 hover:text-white"
                aria-label="Close form"
              >
                ×
              </button>
            </div>

            <form onSubmit={handleSubmit} className="space-y-5">
              <div>
                <label htmlFor="name" className="mb-2 block text-base font-medium text-slate-200">
                  Name
                </label>
                <input
                  id="name"
                  value={name}
                  onChange={(event) => setName(event.target.value)}
                  placeholder="Your name"
                  className="w-full rounded-2xl border border-slate-700 bg-slate-900/80 px-4 py-3.5 text-base text-white placeholder:text-slate-400 outline-none transition duration-200 focus:border-violet-500 focus:ring-2 focus:ring-violet-500/30"
                  required
                />
              </div>

              <div>
                <label htmlFor="message" className="mb-2 block text-base font-medium text-slate-200">
                  Message
                </label>
                <textarea
                  id="message"
                  value={message}
                  onChange={(event) => setMessage(event.target.value)}
                  rows={7}
                  placeholder="Write your message here..."
                  className="w-full rounded-2xl border border-slate-700 bg-slate-900/80 px-4 py-3.5 text-base text-white placeholder:text-slate-400 outline-none transition duration-200 focus:border-violet-500 focus:ring-2 focus:ring-violet-500/30"
                  required
                />
              </div>

              <div className="flex justify-end gap-3 pt-2">
                <button
                  type="button"
                  onClick={() => setIsOpen(false)}
                  className="rounded-full border border-slate-600 bg-transparent px-6 py-3 text-base font-medium text-slate-200 transition hover:border-slate-500 hover:bg-slate-800"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  className="rounded-full bg-violet-600 px-7 py-3 text-base font-semibold text-white shadow-[0_0_12px_rgba(168,85,247,0.2)] transition-all duration-200 ease-out hover:-translate-y-0.5 hover:bg-violet-500 hover:shadow-[0_0_16px_rgba(168,85,247,0.34)]"
                >
                  Send
                </button>
              </div>
            </form>
          </div>
        </div>
      ) : null}
    </div>
  )
}
