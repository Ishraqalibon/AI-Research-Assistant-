<!-- Chosen Palette: Calm Harmony (Warm Neutrals + Emerald Accent) -->
<!-- Application Structure Plan: The structure is a Technical Deep Dive Dashboard utilizing a three-tab main navigation (Pipeline, Stack, Skills). This structure was chosen over a linear report format because the content is highly technical and non-sequential. This allows users (recruiters/academics) to prioritize their exploration: focus on the system's *flow* (Pipeline Tab), the *tools* (Stack Tab), or the *developer's expertise* (Skills Tab). The key interactions are tab switching, clickable flow steps, and interactive chart data visualization. -->
<!-- Visualization & Content Choices: Report Info -> Goal -> Viz/Presentation Method -> Interaction -> Justification -> Library/Method. 1. RAG Steps -> Explain Sequential Logic -> Flow Diagram (HTML/CSS/Tailwind) -> Clickable steps update central text panel -> Clarifies the advanced architecture (Hybrid, Rerank) -> HTML/JS. 2. Technology Stack -> Detail Component Roles -> Interactive Cards/Toggles -> Clicking reveals full role description -> Efficient use of space, user-driven learning -> HTML/JS. 3. Key Learnings -> Quantify Skills -> Horizontal Bar Chart (Chart.js) -> Shows proficiency/focus areas -> Makes abstract skills concrete and measurable -> Chart.js/Canvas. 4. Feature Set -> Summarize Application Utility -> Doughnut Chart (Chart.js) -> Static display of task distribution -> Quick visual overview -> Chart.js/Canvas. CONFIRMATION: NO SVG graphics used. NO Mermaid JS used. -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Research Assistant: Project Deep Dive</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.3/dist/chart.umd.min.js"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        'background-light': '#f9fafb',
                        'card-neutral': '#f3f4f6',
                        'primary': '#10b981', // Emerald 500
                        'secondary-dark': '#1f2937', // Gray 800
                        'accent-blue': '#60a5fa', // Blue 400
                    },
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                    },
                }
            }
        }
    </script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
        .chart-container {
            position: relative;
            width: 100%;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
            height: 320px;
            max-height: 400px;
        }
        .flow-arrow {
            color: #10b981;
            font-size: 2rem;
            line-height: 1;
        }
        .flow-step-active {
            box-shadow: 0 4px 6px -1px rgba(16, 185, 129, 0.4), 0 2px 4px -2px rgba(16, 185, 129, 0.4);
            transform: translateY(-2px);
        }
    </style>
</head>
<body class="bg-background-light min-h-screen font-sans text-secondary-dark antialiased">

    <!-- Global App Container -->
    <div class="max-w-7xl mx-auto p-4 sm:p-6 md:p-8">

        <!-- Header and Title -->
        <header class="text-center py-6 mb-8 bg-white rounded-xl shadow-lg border-b-4 border-primary">
            <h1 class="text-4xl md:text-5xl font-extrabold mb-2 text-secondary-dark">
                📘 AI Research Assistant: Project Deep Dive
            </h1>
            <p class="text-lg text-gray-500 max-w-3xl mx-auto">
                Interactive exploration of the Hybrid RAG Architecture and LangGraph Orchestration.
            </p>
        </header>

        <!-- Main Navigation (Tabs) -->
        <nav class="flex space-x-2 md:space-x-4 border-b border-gray-300 mb-6 sticky top-0 bg-background-light z-10 p-2 -mx-2">
            <button id="tab-pipeline" data-tab="pipeline" class="tab-btn px-4 py-3 text-sm md:text-base font-semibold border-b-4 border-transparent hover:border-primary/50 transition duration-150 ease-in-out text-gray-600 active-tab-style">
                Pipeline Breakdown
            </button>
            <button id="tab-stack" data-tab="stack" class="tab-btn px-4 py-3 text-sm md:text-base font-semibold border-b-4 border-transparent hover:border-primary/50 transition duration-150 ease-in-out text-gray-600">
                Technology Stack
            </button>
            <button id="tab-skills" data-tab="skills" class="tab-btn px-4 py-3 text-sm md:text-base font-semibold border-b-4 border-transparent hover:border-primary/50 transition duration-150 ease-in-out text-gray-600">
                Skills & Outcomes
            </button>
        </nav>

        <!-- Main Content Area -->
        <main class="py-4">
            
            <!-- Tab 1: Pipeline Breakdown -->
            <section id="pipeline-content" class="tab-content">
                <h2 class="text-3xl font-bold mb-4 border-l-4 border-primary pl-3">RAG Architecture Flow: The Path to Grounded Answers</h2>
                <p class="text-gray-600 mb-8">
                    This section breaks down the three critical steps of the advanced Retrieval Augmented Generation (RAG) pipeline. Click on any step to see a detailed explanation of its function and how it improves the accuracy of the final output. The system is designed to overcome the limitations of simple vector search by applying multiple layers of context validation.
                </p>

                <!-- Flow Diagram -->
                <div class="flex flex-col md:flex-row items-center justify-between space-y-4 md:space-y-0 md:space-x-4 mb-10">

                    <!-- Step 1: Hybrid Retrieval -->
                    <div data-flow="hybrid-retrieve" class="flow-step flex-1 w-full p-4 bg-card-neutral rounded-xl shadow-md cursor-pointer border-2 border-transparent hover:border-primary/50 transition duration-200">
                        <div class="text-lg font-bold text-secondary-dark">1. Hybrid Retrieval</div>
                        <p class="text-sm text-gray-500">Dense (Qdrant) + Sparse (BM25)</p>
                    </div>

                    <div class="flow-arrow">➡️</div>

                    <!-- Step 2: Cross-Encoder Reranking -->
                    <div data-flow="reranking" class="flow-step flex-1 w-full p-4 bg-card-neutral rounded-xl shadow-md cursor-pointer border-2 border-transparent hover:border-primary/50 transition duration-200">
                        <div class="text-lg font-bold text-secondary-dark">2. Cross-Encoder Reranking</div>
                        <p class="text-sm text-gray-500">Context Validation & Noise Reduction</p>
                    </div>

                    <div class="flow-arrow">➡️</div>

                    <!-- Step 3: LLM Generation & State -->
                    <div data-flow="langgraph" class="flow-step flex-1 w-full p-4 bg-card-neutral rounded-xl shadow-md cursor-pointer border-2 border-transparent hover:border-primary/50 transition duration-200">
                        <div class="text-lg font-bold text-secondary-dark">3. Stateful Orchestration</div>
                        <p class="text-sm text-gray-500">LangGraph Workflow & LLM Generation</p>
                    </div>
                </div>

                <!-- Interactive Explanation Panel -->
                <div class="bg-white p-6 rounded-xl shadow-2xl border-t-4 border-accent-blue">
                    <h3 id="flow-title" class="text-2xl font-bold mb-3 text-accent-blue">
                        Select a Step Above to Explore the Architecture
                    </h3>
                    <p id="flow-content" class="text-gray-700 leading-relaxed">
                        This panel dynamically updates to provide a deep dive into the technical mechanism, purpose, and specific library used for the selected pipeline stage. Understanding this flow demonstrates mastery over advanced RAG design principles.
                    </p>
                </div>
            </section>

            <!-- Tab 2: Technology Stack -->
            <section id="stack-content" class="tab-content hidden">
                <h2 class="text-3xl font-bold mb-4 border-l-4 border-primary pl-3">Technology Stack: Components & Roles</h2>
                <p class="text-gray-600 mb-8">
                    The core of the project relies on six key technologies working in concert. This combination ensures stability, scalability, and state-of-the-art retrieval performance. Click on any component card to read its specific role in the architecture.
                </p>

                <!-- Charts and Features (Dual Column Layout) -->
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-10">
                    <div class="bg-white p-6 rounded-xl shadow-lg">
                        <h3 class="text-xl font-bold mb-4">Feature Distribution</h3>
                        <p class="text-sm text-gray-500 mb-4">The application's utility is segmented across five key research tasks.</p>
                        <div class="chart-container">
                            <canvas id="featuresChart"></canvas>
                        </div>
                    </div>
                    <div class="bg-white p-6 rounded-xl shadow-lg">
                        <h3 class="text-xl font-bold mb-4">Project Scope & Scale</h3>
                        <p class="text-sm text-gray-500 mb-4">The core focus is on sophisticated retrieval and workflow orchestration.</p>
                        <ul class="space-y-3 text-gray-700">
                            <li class="flex items-center"><span class="text-primary mr-3 text-xl">✓</span> Advanced RAG Pipeline (Hybrid + Reranking)</li>
                            <li class="flex items-center"><span class="text-primary mr-3 text-xl">✓</span> Stateful, Agentic Workflow (LangGraph)</li>
                            <li class="flex items-center"><span class="text-primary mr-3 text-xl">✓</span> Scalable Vector Storage (Qdrant)</li>
                            <li class="flex items-center"><span class="text-primary mr-3 text-xl">✓</span> Responsive UI (Streamlit)</li>
                        </ul>
                        <div class="mt-6 p-4 bg-primary/10 rounded-lg text-primary text-sm font-medium">
                            The technical challenge centered on maximizing context relevance via Cross-Encoder Reranking.
                        </div>
                    </div>
                </div>

                <!-- Stack Cards (Grid) -->
                <div class="grid grid-cols-2 md:grid-cols-3 gap-4">
                    <div data-tech="streamlit" class="tech-card p-4 bg-card-neutral rounded-lg text-center cursor-pointer hover:bg-primary/20 transition duration-150 shadow-md">
                        <span class="text-3xl block mb-1">💻</span>
                        <span class="font-semibold">Streamlit</span>
                    </div>
                    <div data-tech="langgraph" class="tech-card p-4 bg-card-neutral rounded-lg text-center cursor-pointer hover:bg-primary/20 transition duration-150 shadow-md">
                        <span class="text-3xl block mb-1">🔗</span>
                        <span class="font-semibold">LangGraph</span>
                    </div>
                    <div data-tech="qdrant" class="tech-card p-4 bg-card-neutral rounded-lg text-center cursor-pointer hover:bg-primary/20 transition duration-150 shadow-md">
                        <span class="text-3xl block mb-1">🗄️</span>
                        <span class="font-semibold">Qdrant</span>
                    </div>
                    <div data-tech="openai" class="tech-card p-4 bg-card-neutral rounded-lg text-center cursor-pointer hover:bg-primary/20 transition duration-150 shadow-md">
                        <span class="text-3xl block mb-1">🧠</span>
                        <span class="font-semibold">OpenAI (LLM)</span>
                    </div>
                    <div data-tech="bm25" class="tech-card p-4 bg-card-neutral rounded-lg text-center cursor-pointer hover:bg-primary/20 transition duration-150 shadow-md">
                        <span class="text-3xl block mb-1">🔍</span>
                        <span class="font-semibold">BM25 Retrieval</span>
                    </div>
                    <div data-tech="crossencoder" class="tech-card p-4 bg-card-neutral rounded-lg text-center cursor-pointer hover:bg-primary/20 transition duration-150 shadow-md">
                        <span class="text-3xl block mb-1">🏅</span>
                        <span class="font-semibold">Cross-Encoder</span>
                    </div>
                </div>

                <!-- Technology Detail Panel -->
                <div class="mt-8 bg-white p-6 rounded-xl shadow-2xl border-t-4 border-primary">
                    <h3 id="tech-title" class="text-2xl font-bold mb-3 text-primary">
                        Select a Technology Above for Details
                    </h3>
                    <p id="tech-content" class="text-gray-700 leading-relaxed">
                        The success of the RAG system is a direct result of carefully selected and integrated tooling. Each component plays a vital and specialized role in the overall performance.
                    </p>
                </div>

            </section>

            <!-- Tab 3: Skills & Outcomes -->
            <section id="skills-content" class="tab-content hidden">
                <h2 class="text-3xl font-bold mb-4 border-l-4 border-primary pl-3">Skill Showcase & Project Outcomes</h2>
                <p class="text-gray-600 mb-8">
                    This section highlights the specific, high-value technical skills mastered during the development of the advanced RAG system, proving deep understanding of modern GenAI engineering practices.
                </p>

                <!-- Key Learnings Chart (Bar Chart) -->
                <div class="bg-white p-6 rounded-xl shadow-lg mb-10">
                    <h3 class="text-xl font-bold mb-4">Key Technical Skill Proficiency</h3>
                    <p class="text-sm text-gray-500 mb-4">Focus areas demonstrate expertise beyond basic RAG implementation.</p>
                    <div class="chart-container h-80 max-h-[350px]">
                        <canvas id="skillsChart"></canvas>
                    </div>
                </div>
                
                <!-- Future Enhancements -->
                <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                    <div class="p-5 bg-card-neutral rounded-xl shadow-md border-l-4 border-accent-blue">
                        <h4 class="text-xl font-semibold mb-2 flex items-center"><span class="mr-2">🔐</span> User Authentication</h4>
                        <p class="text-gray-700 text-sm">Implement Firebase/Auth0 for user login and private, secured document storage.</p>
                    </div>
                    <div class="p-5 bg-card-neutral rounded-xl shadow-md border-l-4 border-accent-blue">
                        <h4 class="text-xl font-semibold mb-2 flex items-center"><span class="mr-2">🌐</span> External Grounding</h4>
                        <p class="text-gray-700 text-sm">Integrate Google Search or web crawlers to verify facts against the wider internet (External RAG).</p>
                    </div>
                    <div class="p-5 bg-card-neutral rounded-xl shadow-md border-l-4 border-accent-blue">
                        <h4 class="text-xl font-semibold mb-2 flex items-center"><span class="mr-2">⚡</span> Asynchronous Processing</h4>
                        <p class="text-gray-700 text-sm">Refactor PDF processing and Qdrant population for faster, non-blocking UI during large uploads.</p>
                    </div>
                </div>
            </section>

        </main>
    </div>

    <!-- JavaScript Logic -->
    <script>
        const appState = {
            activeTab: 'pipeline',
            flowDetails: {
                'hybrid-retrieve': {
                    title: '1. Hybrid Retrieval (Qdrant + BM25)',
                    content: 'This stage maximizes context recall by combining semantic search (Qdrant for conceptual similarity) and keyword search (BM25 for term exactness). This mitigates the "lost in translation" problem of pure vector search, ensuring key proper nouns and specific terms are always retrieved. This provides a robust set of 10-20 potential context chunks.',
                    color: 'accent-blue'
                },
                'reranking': {
                    title: '2. Cross-Encoder Reranking',
                    content: 'The crucial second stage. A specialized Cross-Encoder model analyzes the relationship between the query and each retrieved chunk, providing a highly accurate relevance score. Only the top 3-5 validated chunks are passed to the LLM. This drastically reduces noise and prevents the LLM from being distracted by marginally related context, which is key to avoiding hallucinations.',
                    color: 'orange'
                },
                'langgraph': {
                    title: '3. Stateful Orchestration (LangGraph)',
                    content: 'LangGraph manages the entire application flow, defining state, nodes, and conditional edges (`route_task` in `utils.py`). This allows the system to reliably switch between complex tasks (Q&A, Summarization, Comparison) based on user intent, ensuring low latency and stateful memory across operations.',
                    color: 'primary'
                }
            },
            techDetails: {
                'streamlit': { title: 'Streamlit: Responsive Frontend', content: 'Used for the entire user interface, document upload management, and creating the interactive web application, ensuring rapid prototyping and a functional user experience.', color: '#059669' },
                'langgraph': { title: 'LangGraph: Workflow Orchestration', content: 'Essential for managing the complex, multi-step agentic workflow. It handles state, branching logic, and sequence decisions for all research modes (Q&A, Summarization, Comparison).', color: '#60a5fa' },
                'qdrant': { title: 'Qdrant: Vector Database', content: 'Provides scalable vector storage and retrieval capabilities for the Dense Retrieval part of the hybrid search. Its efficiency allows for fast, high-volume semantic querying.', color: '#4b5563' },
                'openai': { title: 'OpenAI (LLM): Generation & Reasoning', content: 'The LLM (specifically `gpt-4o-mini`) is used for reasoning, answer synthesis, and generation across all research tools, using the verified context provided by the RAG pipeline.', color: '#000000' },
                'bm25': { title: 'BM25 Retrieval: Keyword Search', content: 'A Sparse Retriever that provides high recall for specific keywords and proper nouns. It is combined with Qdrant via the `EnsembleRetriever` to form the initial hybrid context set.', color: '#ef4444' },
                'crossencoder': { title: 'Cross-Encoder: Reranking Model', content: 'A small, powerful model used to validate the relevance of initial context chunks before they reach the LLM, effectively filtering out noise and significantly boosting final answer quality.', color: '#f59e0b' }
            },
            chartData: {
                features: {
                    labels: ['Q&A', 'Comparative Analysis', 'Summarization', 'Citation Generation', 'Modular Architecture'],
                    data: [35, 25, 20, 10, 10] 
                },
                skills: {
                    labels: [
                        'Advanced RAG Pipeline Design (Hybrid + Reranking)', 
                        'Stateful Agentic Workflows (LangGraph)', 
                        'Integration of Disparate Services (Qdrant, Streamlit)',
                        'Robust PDF Processing & Chunking'
                    ],
                    data: [95, 88, 80, 70] 
                }
            },
            charts: {}
        };

        function switchTab(targetTab) {
            document.querySelectorAll('.tab-content').forEach(el => el.classList.add('hidden'));
            document.getElementById(`${targetTab}-content`).classList.remove('hidden');

            document.querySelectorAll('.tab-btn').forEach(btn => {
                btn.classList.remove('active-tab-style', 'border-primary', 'text-secondary-dark');
                btn.classList.add('border-transparent', 'text-gray-600');
            });
            const activeBtn = document.getElementById(`tab-${targetTab}`);
            activeBtn.classList.add('active-tab-style', 'border-primary', 'text-secondary-dark');
            activeBtn.classList.remove('border-transparent', 'text-gray-600');
            
            appState.activeTab = targetTab;
            // Lazy load charts only when the tab is first viewed
            if (targetTab === 'stack' && !appState.charts.features) {
                initializeFeaturesChart();
            }
            if (targetTab === 'skills' && !appState.charts.skills) {
                initializeSkillsChart();
            }
        }

        function updateFlowDetail(stepKey) {
            const detail = appState.flowDetails[stepKey];
            document.getElementById('flow-title').textContent = detail.title;
            document.getElementById('flow-content').textContent = detail.content;
            document.getElementById('flow-title').className = `text-2xl font-bold mb-3 text-${detail.color}-600`;
            
            document.querySelectorAll('.flow-step').forEach(step => step.classList.remove('flow-step-active', 'border-primary'));
            document.querySelector(`[data-flow="${stepKey}"]`).classList.add('flow-step-active', 'border-primary');
        }

        function updateTechDetail(techKey) {
            const detail = appState.techDetails[techKey];
            document.getElementById('tech-title').textContent = detail.title;
            document.getElementById('tech-content').textContent = detail.content;
            document.getElementById('tech-title').className = `text-2xl font-bold mb-3 text-${detail.color}-600`;
            
            document.querySelectorAll('.tech-card').forEach(card => card.classList.remove('flow-step-active', 'bg-primary/50', 'bg-card-neutral'));
            document.querySelectorAll('.tech-card').forEach(card => card.classList.add('bg-card-neutral'));
            document.querySelector(`[data-tech="${techKey}"]`).classList.add('flow-step-active', 'bg-primary/20');
        }

        function initializeFeaturesChart() {
            const ctx = document.getElementById('featuresChart').getContext('2d');
            appState.charts.features = new Chart(ctx, {
                type: 'doughnut',
                data: {
                    labels: appState.chartData.features.labels,
                    datasets: [{
                        data: appState.chartData.features.data,
                        backgroundColor: ['#10b981', '#60a5fa', '#f59e0b', '#ef4444', '#1f2937'],
                        hoverOffset: 10,
                        borderWidth: 2,
                        borderColor: '#ffffff'
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: { position: 'bottom' },
                        tooltip: { callbacks: { label: (context) => { return `${context.label}: ${context.raw}%`; } } },
                        title: { display: false }
                    }
                }
            });
        }

        function initializeSkillsChart() {
            const ctx = document.getElementById('skillsChart').getContext('2d');
            appState.charts.skills = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: appState.chartData.skills.labels.map(l => l.match(/.{1,16}(\s|$)/g).join('\n').trim()),
                    datasets: [{
                        label: 'Mastery Level (%)',
                        data: appState.chartData.skills.data,
                        backgroundColor: '#10b981',
                        borderColor: '#059669',
                        borderWidth: 1,
                        borderRadius: 4
                    }]
                },
                options: {
                    indexAxis: 'y',
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        x: {
                            beginAtZero: true,
                            max: 100,
                            ticks: { callback: (value) => `${value}%` }
                        },
                        y: {
                            grid: { display: false }
                        }
                    },
                    plugins: {
                        legend: { display: false },
                        tooltip: { 
                            callbacks: { 
                                title: (context) => appState.chartData.skills.labels[context[0].dataIndex],
                                label: (context) => `Mastery: ${context.raw}%`
                            } 
                        }
                    }
                }
            });
        }

        // Initialize event listeners and state
        window.onload = function() {
            document.querySelectorAll('.tab-btn').forEach(btn => {
                btn.addEventListener('click', () => switchTab(btn.dataset.tab));
            });
            document.querySelectorAll('.flow-step').forEach(step => {
                step.addEventListener('click', () => updateFlowDetail(step.dataset.flow));
            });
            document.querySelectorAll('.tech-card').forEach(card => {
                card.addEventListener('click', () => updateTechDetail(card.dataset.tech));
            });

            // Set initial state
            switchTab('pipeline');
            updateFlowDetail('hybrid-retrieve');
        };
    </script>
</body>
</html>
