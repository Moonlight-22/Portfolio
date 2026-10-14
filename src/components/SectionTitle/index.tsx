type SectionTitleProps = {
  eyebrow?: string
  title: string
  subtitle?: string
}

export default function SectionTitle({ eyebrow, title, subtitle }: SectionTitleProps) {
  return (
    <header className="mb-8 text-center md:mb-10">
      {eyebrow ? (
        <p className="mb-2 text-xs font-semibold uppercase tracking-[0.2em] text-sky-400 md:text-sm">{eyebrow}</p>
      ) : null}
      <h2 className="text-2xl font-bold tracking-tight md:text-4xl">{title}</h2>
      {subtitle ? <p className="mx-auto mt-3 max-w-2xl text-sm leading-6 text-slate-600 dark:text-slate-300 md:text-base md:leading-normal">{subtitle}</p> : null}
    </header>
  )
}
