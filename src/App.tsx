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

function PortfolioPage() {
  return (
    <div className="min-h-screen bg-slate-50 text-slate-900 transition-colors dark:bg-slate-950 dark:text-slate-100">
      <Navbar />
      <main>
        <HomeSection />
        <AboutSection />
        <SkillsSection />
        <ProjectsSection />
        <CertificatesSection />
        <ContactSection />
      </main>
      <Footer />
      <ScrollToTop />
    </div>
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
          className="mt-6 inline-flex rounded-full bg-violet-600 px-6 py-3 text-white hover:bg-violet-500"
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
      <Route path="*" element={<NotFoundPage />} />
    </Routes>
  )
}

export default App
