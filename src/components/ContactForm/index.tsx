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
      <div className="relative z-20 rounded-[28px] border border-sky-500/15 bg-[radial-gradient(circle_at_top,_rgba(30,64,175,0.2),_rgba(17,21,27,0.97)_34%,_rgba(5,7,10,1)_100%)] p-4 shadow-[0_25px_90px_rgba(0,0,0,0.7)] transition-all duration-300 ease-out hover:-translate-y-1 hover:shadow-[0_35px_120px_rgba(30,64,175,0.16)] md:rounded-[32px] md:p-8">
        <div className="flex flex-col gap-5 md:flex-row md:items-center md:justify-between">
          <p className="max-w-xl text-sm leading-6 text-slate-200 md:text-lg md:leading-relaxed">
            I’m open to project discussions, collaborations, and business opportunities.
          </p>

          <button
            type="button"
            onClick={() => setIsOpen(true)}
            className="relative z-30 inline-flex w-fit cursor-pointer items-center justify-center rounded-full bg-sky-600 px-5 py-2.5 text-sm font-bold text-white shadow-[0_0_14px_rgba(96,165,250,0.18)] transition-all duration-200 ease-out hover:-translate-y-0.5 hover:bg-sky-500 hover:shadow-[0_0_18px_rgba(96,165,250,0.28)] focus:outline-none focus:ring-2 focus:ring-sky-400/50 md:px-6 md:py-3 md:text-base"
          >
            Send Message
          </button>
        </div>
      </div>

      {isOpen ? (
        <div className="fixed inset-0 z-[100] flex items-center justify-center bg-slate-950/70 p-4 backdrop-blur-sm">
          <div className="relative z-[101] w-full max-w-[720px] rounded-[24px] border border-sky-500/15 bg-[#11151b]/[0.98] p-4 shadow-[0_35px_120px_rgba(0,0,0,0.9)] transition-all duration-300 ease-out animate-[fadeIn_0.2s_ease-out] md:rounded-[30px] md:p-7">
            <div className="mb-6 flex items-center justify-between gap-4">
              <h3 className="text-xl font-semibold tracking-tight text-white md:text-3xl">Send a message</h3>
              <button
                type="button"
                onClick={() => setIsOpen(false)}
                className="flex h-10 w-10 items-center justify-center rounded-full text-2xl text-slate-300 transition hover:bg-slate-800 hover:text-white"
                aria-label="Close form"
              >
                ×
              </button>
            </div>

            <form onSubmit={handleSubmit} className="space-y-4 md:space-y-5">
              <div>
                <label htmlFor="name" className="mb-2 block text-sm font-medium text-slate-200 md:text-base">
                  Name
                </label>
                <input
                  id="name"
                  value={name}
                  onChange={(event) => setName(event.target.value)}
                  placeholder="Your name"
                  className="w-full rounded-2xl border border-slate-700 bg-[#0b0e12] px-4 py-3 text-sm text-white placeholder:text-slate-400 outline-none transition duration-200 focus:border-sky-500 focus:ring-2 focus:ring-sky-500/25 md:py-3.5 md:text-base"
                  required
                />
              </div>

              <div>
                <label htmlFor="message" className="mb-2 block text-sm font-medium text-slate-200 md:text-base">
                  Message
                </label>
                <textarea
                  id="message"
                  value={message}
                  onChange={(event) => setMessage(event.target.value)}
                  rows={7}
                  placeholder="Write your message here..."
                  className="w-full rounded-2xl border border-slate-700 bg-[#0b0e12] px-4 py-3 text-sm text-white placeholder:text-slate-400 outline-none transition duration-200 focus:border-sky-500 focus:ring-2 focus:ring-sky-500/25 md:py-3.5 md:text-base"
                  required
                />
              </div>

              <div className="flex justify-end gap-2 pt-2 md:gap-3">
                <button
                  type="button"
                  onClick={() => setIsOpen(false)}
                  className="rounded-full border border-slate-600 bg-transparent px-5 py-2.5 text-sm font-medium text-slate-200 transition hover:border-slate-500 hover:bg-slate-800 md:px-6 md:py-3 md:text-base"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  className="rounded-full bg-sky-600 px-6 py-2.5 text-sm font-semibold text-white shadow-[0_0_12px_rgba(96,165,250,0.16)] transition-all duration-200 ease-out hover:-translate-y-0.5 hover:bg-sky-500 hover:shadow-[0_0_16px_rgba(96,165,250,0.28)] md:px-7 md:py-3 md:text-base"
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
