import level4 from '../assets/images/Lv4.jpg'
import level5 from '../assets/images/Lv5.jpg'

export type CertificateIndexItem = {
	id: string
	title: string
	issuer: string
	status?: string
	image: string
	url: string
}

export const certificateIndex: CertificateIndexItem[] = [
	{
		id: 'ncc-level-4',
		title: 'NCC Level 4',
		issuer: 'Strategy First University/NCC Education (UK)',
		image: level4,
		url: 'https://example.com',
	},
	{
		id: 'ncc-level-5',
		title: 'NCC Level 5',
		issuer: 'Strategy First University/NCC Education (UK)',
		image: level5,
		url: 'https://example.com',
	},
	{
		id: 'bachelor-computer-science',
		title: 'Bachelor of Science (Hons) in Computer Science',
		issuer: 'Strategy First University / University of Wolverhampton (UK)',
		status: 'Currently waiting for certificate',
		image:
			'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?q=80&w=1200&auto=format&fit=crop',
		url: 'https://example.com',
	},
]
