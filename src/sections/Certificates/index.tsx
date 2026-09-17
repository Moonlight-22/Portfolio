import { certificates } from '../../data/certificates'
import SectionTitle from '../../components/SectionTitle'

export default function CertificatesSection() {
  return (
    <section id="certificates" className="mx-auto max-w-6xl px-4 py-16 md:px-6">
      <SectionTitle eyebrow="Certificates" title="Certifications" subtitle="A responsive showcase of recent learning and achievements." />
      <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
        {certificates.map((certificate) => (
          <a
            key={certificate.title}
            href={certificate.url}
            target="_blank"
            rel="noreferrer"
            className="glass overflow-hidden rounded-3xl border border-white/20 shadow-lg transition hover:-translate-y-1"
          >
            <img src={certificate.image} alt={certificate.title} loading="lazy" className="h-40 w-full object-cover" />
            <div className="p-4">
              <h3 className="font-bold">{certificate.title}</h3>
              <p className="mt-1 text-sm text-slate-600 dark:text-slate-300">{certificate.issuer}</p>
            </div>
          </a>
        ))}
      </div>
    </section>
  )
}
