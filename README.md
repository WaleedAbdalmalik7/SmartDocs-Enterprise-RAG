SmartDocs AI 🏢🤖
مساعد ذكي للمستندات والأنظمة المؤسسية (Enterprise RAG System)
نظام متكامل يسمح للشركات ببناء قواعد معرفة خاصة بها، والسماح للموظفين بالاستعلام عن اللوائح والسياسات والإجراءات باللغة الطبيعية بدقة وأمان تام.

🌟 نظرة عامة
SmartDocs AI ليس مجرد شات بوت تجريبي، بل هو نظام مؤسسي جاهز للإنتاج (Production-Ready) مبني على تقنية RAG (Retrieval-Augmented Generation). يتميز النظام بقدرته على عزل بيانات كل شركة بشكل تام (Multi-Tenancy)، ودعمه القوي للغة العربية، وتوفيره لبيئة آمنة وخاضعة للرقابة للبحث داخل المستندات الداخلية.

✨ المميزات الرئيسية (Enterprise Features)
🏗️ بنية متعددة المستأجرين (Multi-Tenancy): عزل تام للبيانات بين الشركات في قواعد البيانات العلائقية والمتجهة.
🛡️ أمان وصلاحيات (RBAC): نظام مصادقة حقيقي (JWT)، وأدوار (Admin, Manager, Employee, Viewer) تتحكم في الوصول للمستندات والمحادثات.
📚 إدارة الوثائق والإصدارات: رفع ملفات (PDF, DOCX)، دعم الإصدارات المتعددة (Versioning)، والأرشفة التلقائية للنسخ القديمة.
🔍 بحث هجين متقدم (Hybrid Search): دمج بين البحث الدلالي (Semantic) والبحث بالكلمات المفتاحية (Keyword) مع خوارزمية دمج وترتيب ذكية (RRF Reranking).
👁️ دعم OCR: التعرف التلقائي على النصوص داخل الصور والملفات الممسوحة ضوئياً (عربي/إنجليزي).
🧠 محادثات ذكية (Conversational RAG): فهم سياق المحادثة السابقة، وإعادة صياغة الأسئلة المتتابعة.
🛤️ موجه الاستعلامات (Query Router): توجيه ذكي يحدد ما إذا كان السؤال يحتاج بحثاً داخلياً في وثائق الشركة أم بحثاً خارجياً في الويب (المواقع الحكومية).
📡 بث مباشر (Streaming): استلام إجابات الـ LLM بشكل تدريجي مما يوفر تجربة مستخدم سلسة وسريعة.
📑 نظام الاستشهادات (Citations): ربط كل إجابة بالمستند الأصلي، ورقم الصفحة، والإصدار لضمان الموثوقية ومنع الهلوسة (Hallucination).
⚙️ معالجة خلفية (Background Jobs): معالجة الملفات الثقيلة واستخراج النصوص والتضمين خارج مسار الـ API لضمان سرعة الاستجابة.
🛠️ التقنيات المستخدمة (Tech Stack)
الـ Backend و الـ API:

PythonPython 3.11+
FastAPIFastAPI
PostgreSQLPostgreSQL
SQLAlchemySQLAlchemy (ORM & Migrations)
الذكاء الاصطناعي والـ RAG:

LangChainLangChain
GroqLlama 3.3 70B (via Groq API)
BGE-M3BGE-M3 (Multilingual Embeddings)
ChromaChromaDB (Vector Store)
معالجة المستندات:

PyMuPDFPDF Text Extraction
python-docxDOCX Processing
TesseractOCR for Scanned Docs
📁 هيكل المشروع
المشروع مبني بنية معمارية نظيفة (Clean Architecture) تفصل بين طبقات العرض، المنطق، والبيانات:

smartdocs-enterprise-rag/├── app/│   ├── api/                # نقاط النهاية (FastAPI Endpoints & Auth)│   ├── core/               # الإعدادات، الأمان، الاستثناءات│   ├── db/                 # نماذج قاعدة البيانات (SQLAlchemy Models)│   ├── rag/                # محرك الذكاء الاصطناعي (Embeddings, Retriever, Generator)│   ├── schemas/            # نماذج التحقق (Pydantic Schemas)│   └── services/           # منطق الأعمال (رفع الملفات، السجلات)├── storage/                # التخزين المحلي للملفات├── alembic/                # تهجيرات قاعدة البيانات (Migrations)├── .env.example            # متغيرات البيئة└── requirements.txt        # المتطلبات
