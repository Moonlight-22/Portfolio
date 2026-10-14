import ContactForm from '../../components/ContactForm'
import SectionTitle from '../../components/SectionTitle'

export default function ContactSection() {
  return (
    <section id="contact" className="mx-auto max-w-6xl px-4 py-12 md:px-6 md:py-16">
      <SectionTitle
        eyebrow="Contact"
        title="Let’s Connect"
        subtitle="Have an idea, a collaboration, or a new opportunity? Send a quick message and I’ll get back to you soon."
      />
      <ContactForm />
    </section>
  )
}
