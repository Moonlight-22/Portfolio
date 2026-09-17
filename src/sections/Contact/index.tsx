import ContactForm from '../../components/ContactForm'
import SectionTitle from '../../components/SectionTitle'

export default function ContactSection() {
  return (
    <section id="contact" className="mx-auto max-w-6xl px-4 py-16 md:px-6">
      <SectionTitle eyebrow="Contact" title="Let's Work Together" subtitle="Have an idea or opportunity? Send a message and I will get back to you soon." />
      <ContactForm />
    </section>
  )
}
