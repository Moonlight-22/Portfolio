export type Certificate = {
  title: string
  issuer: string
  image: string
  url: string
}

export const certificates: Certificate[] = [
  {
    title: 'NCC Level 4',
    issuer: 'Strategy First University',
    image:
      'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?q=80&w=1200&auto=format&fit=crop',
    url: 'https://example.com',
  },
  {
    title: 'NCC Level 5',
    issuer: 'Strategy First University',
    image:
      'https://images.unsplash.com/photo-1522202176988-66273c2fd55f?q=80&w=1200&auto=format&fit=crop',
    url: 'https://example.com',
  },
  {
    title: 'Spring Boot Professional',
    issuer: 'LinkedIn Learning',
    image:
      'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?q=80&w=1200&auto=format&fit=crop',
    url: 'https://example.com',
  },
]
