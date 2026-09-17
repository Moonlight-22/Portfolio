type SectionTitleProps = {
  eyebrow?: string
  title: string
  subtitle?: string
}

export default function SectionTitle({ eyebrow, title, subtitle }: SectionTitleProps) {
  return (
    <header className="mb-10 text-center">
      {eyebrow ? (
        <p className="mb-2 text-sm font-semibold uppercase tracking-[0.2em] text-violet-500">{eyebrow}</p>
      ) : null}
      <h2 className="text-3xl font-bold tracking-tight md:text-4xl">{title}</h2>
      {subtitle ? <p className="mx-auto mt-3 max-w-2xl text-slate-600 dark:text-slate-300">{subtitle}</p> : null}
    </header>
  )
}
