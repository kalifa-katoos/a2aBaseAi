# A2ABase Clone - Proof of Concept

هذا المشروع هو بداية لبناء منصة مشابهة لـ a2abase.ai باستخدام بروتوكول A2A.

## الإعداد (Setup)
1. قم بإنشاء بيئة افتراضية (تم إنشاؤها بالفعل):
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```
2. قم بتثبيت المكتبات:
   ```bash
   pip install a2a-sdk python-dotenv
   ```
3. أضف مفتاح الـ API الخاص بك في ملف `.env`:
   - `A2ABASE_API_KEY`: مفتاح المنصة.
   - `GEMINI_API_KEY`: مفتاح Gemini.

## التشغيل (Run)
قم بتشغيل وكيل الواجهة البسيط:
```bash
python simple_agent.py
```

## المكونات الحالية
- `simple_agent.py`: نموذج أولي لوكيل (Agent) يقوم بالتعريف بنفسه.
- `.env`: ملف لإدارة مفاتيح الـ API.
- `dashboard/`: منصة الويب المبنية بـ Next.js لإدارة الوكلاء.

## التوثيق (Documentation)
يمكنك الإطلاع على الدليل الكامل للمطورين في ملف **[docs/GUIDE.md](file:///h:/google/a2aBaseAi/docs/GUIDE.md)**.

## الاختبار النهائي (Final Verification)
للتأكد من أن جميع الأنظمة تعمل بشكل صحيح، قم بتشغيل:
```bash
python verify_final.py
```

## ملاحظات التسليم
- تم تنفيذ بروتوكول A2A بالكامل.
- تم إعداد نظام الذاكرة والتنسيق الذكي.
- تم بناء لوحة تحكم عصرية بـ Next.js.
- تم إعداد بيئات التشغيل عبر Docker.
