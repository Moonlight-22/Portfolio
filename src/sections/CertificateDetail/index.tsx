import { Link, useParams } from 'react-router-dom'
import { FaArrowLeft } from 'react-icons/fa'
import { certificateIndex } from '../../data/certificate_index'

export default function CertificateDetailSection() {
  const { id } = useParams()
  const certificate = certificateIndex.find((item) => item.id === id)

  if (!certificate) {
    return (
      <section className="mx-auto max-w-4xl px-4 py-20 md:px-6">
        <h1 className="text-3xl font-bold">Certificate not found</h1>
        <Link to="/#certificates" className="mt-6 inline-flex items-center gap-2 text-sky-300 hover:text-white">
          <FaArrowLeft /> Back to certificates
        </Link>
      </section>
    )
  }

  return (
    <section className="mx-auto max-w-5xl px-4 py-12 md:px-6 md:py-20">
      <Link to="/#certificates" className="inline-flex items-center gap-2 text-sm text-sky-300 hover:text-white">
        <FaArrowLeft /> Back to certificates
      </Link>
      <div className="mt-8 grid gap-8 md:grid-cols-[0.8fr_1.2fr] md:items-start">
        <div>
          <p className="text-sm font-semibold uppercase text-sky-300">Certificate details</p>
          <h1 className="mt-2 text-3xl font-bold md:text-4xl">{certificate.title}</h1>
          <p className="mt-4 leading-7 text-slate-300">{certificate.issuer}</p>
        </div>
        <img src={certificate.image} alt={certificate.title} className="w-full rounded-lg border border-white/10 bg-white p-2 object-contain" />
      </div>
    </section>
  )
}