export type DocumentIndexItem = {
	projectId: string
	title: string
}

export type DocumentSection = {
	title: string
	paragraph?: string
	items?: string[]
	code?: string
	apiEndpoints?: { method: string; endpoint: string; description: string }[]
}

export const documentIndex: DocumentIndexItem[] = [
	{ projectId: 'eco-tech', title: 'Eco Tech Project Document' },
	{ projectId: 'find-ace', title: 'Find Ace Project Overview' },
	{ projectId: 'android-app', title: 'Android App Project Document' },
	{ projectId: 'portfolio-website', title: 'Portfolio Website Project Document' },
]

export const projectDocumentSections: Record<string, DocumentSection[]> = {
	'eco-tech': [
		{
			title: 'Features',
			items: [
				'Hybrid food data pipeline using the Open Food Facts API with a Scikit-Learn fallback.',
				'BMR calculator using the Mifflin-St Jeor equation.',
				'Calorie and carbon inventory tracking.',
				'Expiration alerts for items within three days of expiry.',
				'Sustainability analytics dashboard with Recharts.',
				'Liquid-glass interface built with Tailwind CSS.',
				'OCR image upload workflow and an admin system summary.',
			],
		},
		{
			title: 'Technology Stack',
			items: [
				'Frontend: React, Vite, Tailwind CSS v4, Recharts, and React Router.',
				'Backend: Python Flask.',
				'Database: MySQL, with SQLite preview mode supported.',
				'Machine learning: TfidfVectorizer and RandomForestRegressor.',
			],
		},
		{
			title: 'Backend Setup',
			paragraph: 'Install the backend dependencies and train the machine-learning models:',
			code: 'cd ecotech_backend\npython -m pip install -r requirements.txt\npython train_models.py\npython train_image_classifier.py --source local --epochs 6',
		},
		{
			title: 'Database Configuration',
			paragraph: 'Set the MySQL connection environment variables before starting the backend:',
			code: '$env:MYSQL_HOST="localhost"\n$env:MYSQL_USER="root"\n$env:MYSQL_PASSWORD="your-password"\n$env:MYSQL_DATABASE="ecotech"',
		},
		{
			title: 'SQLite Preview Mode',
			paragraph: 'Run the backend without MySQL using SQLite preview mode:',
			code: '$env:ECOTECH_DB_DRIVER="sqlite"\npython app.py',
		},
		{
			title: 'OCR Image Upload',
			paragraph:
				'Tesseract is required for receipt and food image OCR. On Windows, the backend auto-detects the default installation path; override it with TESSERACT_CMD if needed.',
			code: 'winget install UB-Mannheim.TesseractOCR\n$env:TESSERACT_CMD="C:\\path\\to\\tesseract.exe"',
		},
		{
			title: 'Food Image Classification',
			paragraph:
				'The first local run downloads sample images from Wikimedia Commons if data/food_images/ is empty. You can also use your own images under data/food_images/<FoodName>/*.jpg and update data/food_image_manifest.csv.',
			code: 'python bootstrap_food_images.py\npython train_image_classifier.py --source local --epochs 6',
		},
		{
			title: 'Database Migration',
			paragraph: 'Apply the sustainability migration to an existing MySQL database:',
			code: 'mysql -u root -p < migrations/20260602_sustainability_upgrade.sql',
		},
		{
			title: 'Frontend Setup',
			paragraph: 'Install and run the frontend, then open http://127.0.0.1:5173:',
			code: 'cd ecotech_frontend\nnpm install\nnpm run dev',
		},
		{
			title: 'API Endpoints',
			apiEndpoints: [
				{ method: 'POST', endpoint: '/api/calculate-bmr', description: 'Calculate and store the daily calorie goal.' },
				{ method: 'POST', endpoint: '/api/process-food', description: 'Run the hybrid food pipeline and store inventory.' },
				{ method: 'GET', endpoint: '/api/expiration-alerts', description: 'Find items expiring within three days.' },
				{ method: 'GET', endpoint: '/api/analytics', description: 'Get sustainability summary metrics.' },
				{ method: 'GET', endpoint: '/api/analytics/weekly', description: 'Get weekly consumed, expired, and carbon metrics.' },
				{ method: 'GET', endpoint: '/api/analytics/monthly', description: 'Get monthly carbon saved and wasted.' },
				{ method: 'GET', endpoint: '/api/analytics/waste-categories', description: 'Group expired items by category.' },
				{ method: 'GET', endpoint: '/api/analytics/insights', description: 'Get dynamic sustainability insights.' },
			],
		},
		{
			title: 'ML Dataset',
			paragraph:
				'train_models.py generates a 3,000-row training dataset. Replace data/food_reference_dataset.csv with labeled data using the columns food_name, category, calories_per_100g, and carbon_footprint_kgCO2e, then rerun training.',
		},
		{
			title: 'Project Structure',
			code: 'project_ecotech/\n├── ecotech_backend/\n│   ├── app.py\n│   ├── analytics_engine.py\n│   ├── bmr.py\n│   ├── food_pipeline.py\n│   ├── ml_predictor.py\n│   ├── open_food_facts.py\n│   ├── train_models.py\n│   ├── data/\n│   ├── models/\n│   └── migrations/\n└── ecotech_frontend/\n    └── src/\n        ├── pages/\n        ├── components/\n        └── layouts/',
		},
	],
	'find-ace': [
		{
			title: 'Features',
			items: [
				'Clients search workers by category, skill, name, and location; send job requests; track progress; and save favorite workers.',
				'Clients can review completed jobs, report issues, and view warranties.',
				'Workers manage profiles, skills, portfolios, and availability, then accept or reject requests and update job status.',
				'Workers receive notifications and warranties, and can report clients after completed jobs.',
				'Admins manage users, workers, jobs, reviews, categories, reports, and warranties through a dashboard.',
				'Users receiving five or more warranties within 24 hours are temporarily banned for one day.',
			],
		},
		{
			title: 'Technology Stack',
			items: [
				'Frontend: React 19, Vite, Tailwind CSS, and Leaflet.',
				'Backend: Laravel 8, PHP 8, and Laravel Sanctum.',
				'Database: MySQL.',
			],
		},
		{
			title: 'Requirements',
			items: ['Node.js 18 or newer', 'PHP 8.0 or newer', 'Composer', 'MySQL (XAMPP recommended on Windows)', 'Apache or the PHP built-in development server'],
		},
		{
			title: 'Backend Setup',
			paragraph: 'Install backend dependencies, configure the database in .env, then initialize and start the API:',
			code: 'cd findAce_Backend\ncomposer install\ncopy .env.example .env\nphp artisan key:generate\n\n# Configure DB_CONNECTION, DB_HOST, DB_PORT, DB_DATABASE, DB_USERNAME, and DB_PASSWORD in .env\nphp artisan migrate\nphp artisan db:seed --class=DemoAccountsSeeder\nphp artisan storage:link\nphp artisan serve --host=127.0.0.1 --port=8000',
		},
		{
			title: 'Frontend Setup',
			paragraph: 'Set the API URL in Frontend/.env, then install dependencies and start the development server:',
			code: 'cd Frontend\nnpm install\n\n# Frontend/.env\nVITE_API_URL=http://127.0.0.1:8000/api\n\nnpm run dev',
		},
		{
			title: 'API Endpoints',
			paragraph: 'The API base URL is http://127.0.0.1:8000/api.',
			apiEndpoints: [
				{ method: 'POST', endpoint: '/api/v1/auth/login', description: 'Sign in to an existing account.' },
				{ method: 'POST', endpoint: '/api/v1/auth/register', description: 'Register as a client or worker.' },
				{ method: 'GET', endpoint: '/api/v1/workers/search', description: 'Search workers by relevant criteria.' },
				{ method: 'POST', endpoint: '/api/v1/job-requests', description: 'Send a job request to a worker.' },
				{ method: 'PATCH', endpoint: '/api/v1/job-requests/{id}/status', description: 'Update a job request status.' },
				{ method: 'POST', endpoint: '/api/v1/reviews', description: 'Submit a review.' },
				{ method: 'POST', endpoint: '/api/v1/reports', description: 'Submit a report.' },
				{ method: 'GET', endpoint: '/api/v1/admin/dashboard', description: 'View the admin dashboard summary.' },
				{ method: 'POST', endpoint: '/api/v1/admin/reports/{id}/warranty', description: 'Issue a warranty for a report.' },
			],
		},
		{
			title: 'Job Status Flow',
			code: 'pending → accepted → in_progress → completed\n         ↘ rejected\npending / accepted → cancelled (client)',
		},
		{
			title: 'Warranty and Ban Rules',
			items: [
				'Admins issue a warranty to the reporter, reported user, or both, with a start and end date.',
				'Warranty dates are stored as warranty_started_at and warranty_ended_at.',
				'Users receive a notification and can view warranty dates in their history.',
				'Five or more warranties within 24 hours trigger a one-day ban.',
			],
		},
		{
			title: 'Project Structure',
			code: 'Final/\n├── Frontend/           # React application\n└── findAce_Backend/    # Laravel API',
		},
		{
			title: 'Notes',
			items: [
				'Sign-in uses the account role; it does not ask users to choose Client or Worker.',
				'Registration lets users choose Client or Worker.',
				'Workers select skills from existing service categories.',
				'Deleting a category in Admin permanently removes it from the database.',
			],
		},
		{
			title: 'License',
			paragraph: 'This project is for academic and final-year project use.',
		},
	],
	'android-app': [
		{
			title: 'Project Overview',
			paragraph:
				'Offline Social is an offline-first Android blogging app for creating, editing, searching, viewing, and deleting posts. Posts and media references are stored locally in SQLite, with optional Android sharing and Facebook upload.',
		},
		{
			title: 'Technology and Platform',
			items: [
				'Android Studio and Java, using the Gradle build system.',
				'Minimum SDK 24 and target SDK 34.',
				'Material Components for the interface, RecyclerView for the post feed, and SearchView for keyword filtering.',
				'SQLite persistence with MessageDbHelper and MessageDao.',
				'Light and dark themes follow the system theme.',
			],
		},
		{
			title: 'Features',
			items: [
				'Create, edit, view, search, and delete posts while offline.',
				'Delete one post or select multiple posts for bulk deletion.',
				'Attach images from the camera or gallery.',
				'Share posts with Android share intents.',
				'Upload an individual post or selected posts through Facebook.',
				'Persist posts in SQLite so they remain available after restarting the app.',
			],
		},
		{
			title: 'System Design',
			paragraph:
				'The app loads posts from SQLite into a RecyclerView. User actions update the database and refresh the feed. UI activities handle post lists, editing, and details; model and data-access classes represent messages and persistence; helper classes handle images, sharing, and Facebook upload.',
		},
		{
			title: 'Main Components',
			items: [
				'MessageListActivity: feed, search, multi-selection, bulk deletion, and group Facebook upload.',
				'MessageEditActivity: create or edit posts and attach camera or gallery images.',
				'MessageDetailActivity: view, edit, share, upload, or delete an individual post.',
				'Message: post model; MessageDao and MessageDbHelper: SQLite data access and schema.',
				'MessageAdapter: RecyclerView binding and selected-item tracking.',
				'ImageHelper, ShareHelper, and FacebookUploadHelper: media and sharing utilities.',
			],
		},
		{
			title: 'Functional Test Results',
			items: [
				'T01-T03: Create, edit, and search posts — passed.',
				'T04-T05: Delete one post and bulk-delete selected posts — passed.',
				'T06-T07: Attach images from gallery and camera — passed.',
				'T08-T10: Android sharing, Facebook upload, and group upload — passed.',
				'T11: SQLite data persists after restarting the app — passed.',
			],
		},
		{
			title: 'Development Challenges and Decisions',
			items: [
				'ImageHelper normalizes camera and gallery image URIs to app-accessible paths so media can be displayed and shared consistently.',
				'MessageAdapter tracks selected post IDs so multi-delete selections remain stable when search results refresh.',
				'Facebook upload uses Android intents to support publishing through the user’s Facebook app without requiring app-specific API keys or OAuth tokens.',
				'Semantic colors in values and values-night improve readability in light and dark themes.',
			],
		},
		{
			title: 'Conclusion and Future Work',
			paragraph:
				'Offline Social demonstrates local post management, SQLite persistence, media attachment, Android intent sharing, and Facebook upload. Potential future additions include cloud sync, richer formatting, post categories, and user profiles.',
		},
		{
			title: 'References',
			items: [
				'Android Developers — Save data using SQLite: https://developer.android.com/training/data-storage/sqlite',
				'Android Developers — RecyclerView: https://developer.android.com/develop/ui/views/layout/recyclerview',
				'Android Developers — Sending simple data to other apps: https://developer.android.com/training/sharing/send',
				'Android Developers — Intents and Intent Filters: https://developer.android.com/guide/components/intents-filters',
				'AndroidX — FileProvider: https://developer.android.com/reference/androidx/core/content/FileProvider',
			],
		},
	],
	'portfolio-website': [
		{
			title: 'Project Overview',
			paragraph:
				'A React and TypeScript application powered by Vite, with hot module replacement for development and Oxlint rules for code quality.',
		},
		{
			title: 'Technology Stack',
			items: ['React', 'TypeScript', 'Vite', 'Oxlint'],
		},
		{
			title: 'Official React Plugins',
			items: [
				'@vitejs/plugin-react uses Oxc for React Fast Refresh.',
				'@vitejs/plugin-react-swc uses SWC for React Fast Refresh.',
			],
		},
		{
			title: 'React Compiler',
			paragraph:
				'The React Compiler is not enabled by default because it can affect development and build performance. Follow the official React Compiler installation guide to enable it.',
		},
		{
			title: 'Expanding the Oxlint Configuration',
			paragraph:
				'For production applications, add oxlint-tsgolint and enable type-aware linting with React and TypeScript rules:',
			code: '{\n  "$schema": "./node_modules/oxlint/configuration_schema.json",\n  "plugins": ["react", "typescript", "oxc"],\n  "options": {\n    "typeAware": true\n  },\n  "rules": {\n    "react/rules-of-hooks": "error",\n    "react/only-export-components": ["warn", { "allowConstantExport": true }]\n  }\n}',
		},
		{
			title: 'Further Reading',
			items: [
				'React Compiler installation: https://react.dev/learn/react-compiler/installation',
				'Oxlint rules: https://oxc.rs/docs/guide/usage/linter/rules',
			],
		},
	],
}
