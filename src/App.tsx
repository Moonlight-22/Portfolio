import type { PropsWithChildren } from 'react'
import { Route, Routes } from 'react-router-dom'
import Navbar from './components/Navbar'
import Footer from './components/Footer'
import ScrollToTop from './components/ScrollToTop'
import HomeSection from './sections/Home'
import AboutSection from './sections/About'
import SkillsSection from './sections/Skills'
import ProjectsSection from './sections/Projects'
import CertificatesSection from './sections/Certificates'
import ContactSection from './sections/Contact'
import DocumentDetailSection from './sections/DocumentDetail'
import CertificateDetailSection from './sections/CertificateDetail'

function SiteLayout({ children }: PropsWithChildren) {
  return (
    <div className="dark relative min-h-screen overflow-x-clip bg-[#05070a] pb-20 text-slate-100 selection:bg-sky-500/30 selection:text-white md:pb-0">
      <div className="pointer-events-none fixed inset-0 -z-10 bg-[radial-gradient(circle_at_top,_rgba(59,130,246,0.12),_transparent_32%),radial-gradient(circle_at_bottom_right,_rgba(96,165,250,0.07),_transparent_28%)]" />
      <Navbar />
      <main className="relative">{children}</main>
      <Footer />
      <ScrollToTop />
    </div>
  )
}

function PortfolioPage() {
  return (
    <SiteLayout>
      <HomeSection />
      <AboutSection />
      <SkillsSection />
      <ProjectsSection />
      <CertificatesSection />
      <ContactSection />
    </SiteLayout>
  )
}

function DocumentPage() {
  return (
    <SiteLayout>
      <DocumentDetailSection />
    </SiteLayout>
  )
}

function CertificatePage() {
  return (
    <SiteLayout>
      <CertificateDetailSection />
    </SiteLayout>
  )
}

function NotFoundPage() {
  return (
    <main className="grid min-h-screen place-items-center px-6">
      <div className="text-center">
        <h1 className="text-6xl font-bold">404</h1>
        <p className="mt-3 text-slate-600 dark:text-slate-300">Page not found.</p>
        <a
          href="/"
          className="mt-6 inline-flex rounded-full bg-sky-600 px-6 py-3 text-white hover:bg-sky-500"
        >
          Back Home
        </a>
      </div>
    </main>
  )
}

function App() {
  return (
    <Routes>
      <Route path="/" element={<PortfolioPage />} />
      <Route path="/documents/:id" element={<DocumentPage />} />
      <Route path="/certificates/:id" element={<CertificatePage />} />
      <Route path="*" element={<NotFoundPage />} />
    </Routes>
  )
}

export default App
