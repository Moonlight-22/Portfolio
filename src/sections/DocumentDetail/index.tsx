import { Link, useParams } from 'react-router-dom'
import { FaArrowLeft, FaGithub } from 'react-icons/fa'
import { documentIndex } from '../../data/document'
import { projects } from '../../data/projects'

export default function DocumentDetailSection() {
  const { id } = useParams()
  const document = documentIndex.find((item) => item.projectId === id)
  const project = projects.find((item) => item.id === id)

  if (!document || !project) {
    return (
      <section className="mx-auto max-w-4xl px-4 py-20 md:px-6">
        <h1 className="text-3xl font-bold">Document not found</h1>
        <Link to="/#projects" className="mt-6 inline-flex items-center gap-2 text-sky-300 hover:text-white">
          <FaArrowLeft /> Back to projects
        </Link>
      </section>
    )
  }

  return (
    <section className="mx-auto max-w-5xl px-4 py-12 md:px-6 md:py-20">
      <Link to="/#projects" className="inline-flex items-center gap-2 text-sm text-sky-300 hover:text-white">
        <FaArrowLeft /> Back to projects
      </Link>
      <div className="mt-8 grid gap-8 md:grid-cols-[1.2fr_0.8fr] md:items-start">
        <div>
          <p className="text-sm font-semibold uppercase text-sky-300">Project document</p>
          <h1 className="mt-2 text-3xl font-bold md:text-4xl">{document.title}</h1>
          <p className="mt-5 leading-7 text-slate-300">{project.description}</p>
          <h2 className="mt-8 text-lg font-semibold">Technologies</h2>
          <ul className="mt-3 flex flex-wrap gap-2">
            {project.technologies.map((technology) => (
              <li key={technology} className="rounded-full border border-white/15 px-3 py-1 text-sm text-slate-200">
                {technology.trim()}
              </li>
            ))}
          </ul>
          {project.githubUrl && project.githubUrl !== 'https://github.com/' ? (
            <a href={project.githubUrl} target="_blank" rel="noreferrer" className="mt-8 inline-flex items-center gap-2 rounded-md bg-sky-600 px-4 py-2 text-sm font-semibold text-white hover:bg-sky-500">
              <FaGithub /> View source
            </a>
          ) : null}
        </div>
        <img src={project.image} alt={project.title} className="w-full rounded-lg border border-white/10 object-cover" />
      </div>
    </section>
  )
}