# RD Report: ONLYOFFICE DesktopEditors + Node Banana

**Date:** 2026-04-23

## ONLYOFFICE DesktopEditors

**What it is:** Open-source office suite (AGPL-3.0) with 4.7k stars — documents, spreadsheets, presentations, PDFs, PDF forms. Cross-platform (Win/Mac/Linux). AI assistants built-in. Plugins API.

**What we'd use it for:** JackConnect agents create/edit CMA reports, contracts, listing agreements, and client documents. Real estate agents need Office compatibility.

**How it fits JackConnect:** Pre-install in JackConnect.exe for real estate clients. Agents use ONLYOFFICE SDK via CLI for document automation.

**Recommendation:** SKILL — add to JackConnect pre-install stack.

---

## Node Banana

**What it is:** Visual node-based workflow editor for AI media generation (1.4k stars, MIT). Drag-drop canvas for chaining AI APIs. Supports Google Gemini, Replicate, fal.ai, Kie.ai, WaveSpeed, OpenAI, Anthropic. Dynamic prompting, prompt chaining, image/video/audio/3D generation, full-screen annotation.

**What we'd use it for:** Visual automation builder for TimeSaverAI. Users drag nodes to chain AI tasks — image → annotate → post to social. Maps to "AI automation creation" feature.

**How it fits:** Integrate as the visual automation canvas alongside CLI automation creation. Kie.ai (already in JackConnect) is a supported provider.

**Recommendation:** INTEGRATE — clone to `/home/workspace/Skills/node-banana/` for visual automation builder.

---

## Verdict

| Repo | Stars | License | Rec | Why |
|------|-------|---------|-----|-----|
| ONLYOFFICE/DesktopEditors | 4.7k | AGPL-3.0 | SKILL | Office suite for RE agents |
| shrimbly/node-banana | 1.4k | MIT | INTEGRATE | Visual automation canvas |