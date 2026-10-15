import { Link, useParams } from 'react-router-dom'
import { FaArrowLeft, FaGithub } from 'react-icons/fa'
import { documentIndex, projectDocumentSections } from '../../data/document'
import { projects } from '../../data/projects'

export default function DocumentDetailSection() {
  const { id } = useParams()
  const document = documentIndex.find((item) => item.projectId === id)
  const project = projects.find((item) => item.id === id)
  const detailSections = id ? projectDocumentSections[id] : undefined

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
      {detailSections ? (
        <div className="mt-12 space-y-6">
          {detailSections.map((section) => (
            <article key={section.title} className="glass rounded-2xl p-5 md:p-7">
              <h2 className="text-xl font-semibold text-white">{section.title}</h2>
              {section.paragraph ? (
                <p className="mt-3 text-left leading-7 text-slate-300">{section.paragraph}</p>
              ) : null}
              {section.items ? (
                <ul className="mt-4 list-disc space-y-2 pl-5 text-left leading-6 text-slate-300 marker:text-sky-400">
                  {section.items.map((item) => <li key={item}>{item}</li>)}
                </ul>
              ) : null}
              {section.code ? (
                <pre className="mt-4 overflow-x-auto whitespace-pre-wrap break-words rounded-xl border border-white/10 bg-black/30 p-4 text-left text-sm leading-6 text-sky-100">
                  <code>{section.code}</code>
                </pre>
              ) : null}
              {section.apiEndpoints ? (
                <div className="mt-4 space-y-3">
                  {section.apiEndpoints.map((api) => (
                    <div
                      key={`${api.method}-${api.endpoint}`}
                      className="grid gap-1 rounded-xl border border-white/10 bg-black/20 p-3 text-left sm:grid-cols-[4rem_minmax(0,1fr)] sm:gap-3"
                    >
                      <span className="text-xs font-bold text-sky-300">{api.method}</span>
                      <div>
                        <code className="break-all text-sm text-slate-100">{api.endpoint}</code>
                        <p className="mt-1 text-sm text-slate-400">{api.description}</p>
                      </div>
                    </div>
                  ))}
                </div>
              ) : null}
            </article>
          ))}
        </div>
      ) : null}
    </section>
  )
}