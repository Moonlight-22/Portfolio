import { useRef, useState } from 'react'
import emailjs from '@emailjs/browser'

type Status = 'idle' | 'loading' | 'success' | 'error'

const SERVICE_ID = import.meta.env.VITE_EMAILJS_SERVICE_ID
const TEMPLATE_ID = import.meta.env.VITE_EMAILJS_TEMPLATE_ID
const PUBLIC_KEY = import.meta.env.VITE_EMAILJS_PUBLIC_KEY

export default function ContactForm() {
  const formRef = useRef<HTMLFormElement>(null)
  const [status, setStatus] = useState<Status>('idle')
  const [message, setMessage] = useState('')

  const onSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault()
    if (!formRef.current) return
    if (!SERVICE_ID || !TEMPLATE_ID || !PUBLIC_KEY) {
      setStatus('error')
      setMessage('EmailJS environment variables are missing.')
      return
    }

    setStatus('loading')
    try {
      await emailjs.sendForm(SERVICE_ID, TEMPLATE_ID, formRef.current, { publicKey: PUBLIC_KEY })
      formRef.current.reset()
      setStatus('success')
      setMessage('Message sent successfully.')
    } catch {
      setStatus('error')
      setMessage('Failed to send message. Please try again.')
    }
  }

  return (
    <form ref={formRef} onSubmit={onSubmit} className="glass rounded-3xl border border-white/20 p-6 shadow-lg">
      <div className="grid gap-4 md:grid-cols-2">
        <input required name="name" placeholder="Name" className="rounded-xl border border-slate-300 bg-white/80 px-4 py-3 outline-none focus:ring-2 focus:ring-violet-500 dark:border-slate-700 dark:bg-slate-900/70" />
        <input required name="email" type="email" placeholder="Email" className="rounded-xl border border-slate-300 bg-white/80 px-4 py-3 outline-none focus:ring-2 focus:ring-violet-500 dark:border-slate-700 dark:bg-slate-900/70" />
      </div>
      <input required name="subject" placeholder="Subject" className="mt-4 w-full rounded-xl border border-slate-300 bg-white/80 px-4 py-3 outline-none focus:ring-2 focus:ring-violet-500 dark:border-slate-700 dark:bg-slate-900/70" />
      <textarea required name="message" rows={5} placeholder="Message" className="mt-4 w-full rounded-xl border border-slate-300 bg-white/80 px-4 py-3 outline-none focus:ring-2 focus:ring-violet-500 dark:border-slate-700 dark:bg-slate-900/70" />
      <button type="submit" disabled={status === 'loading'} className="mt-4 rounded-full bg-violet-600 px-6 py-3 font-semibold text-white transition hover:bg-violet-500 disabled:opacity-70">
        {status === 'loading' ? 'Sending...' : 'Send Message'}
      </button>
      {status !== 'idle' ? (
        <p className={`mt-3 text-sm ${status === 'success' ? 'text-emerald-600' : 'text-rose-600'}`}>{message}</p>
      ) : null}
    </form>
  )
}
