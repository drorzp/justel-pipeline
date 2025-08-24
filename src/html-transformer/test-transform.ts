import { transformArticleHtml, TransformationInput } from './transform-html';
import * as dotenv from 'dotenv';
import * as fs from 'fs';
import * as path from 'path';

// Load .env from the project root
dotenv.config({ path: path.join(__dirname, '../../.env') });

// Mock data provided by user
const mockData: TransformationInput = {
  document_number: "1927030201",
  article_number: "201/9/6",
  main_text: `<article class="legal-article" id="art-201/9/6"><header class="article-header"><h2 class="article-number">Article 201/9/6</h2></header><div class="article-content"><section class="paragraph" id="para-1er"><h3 class="paragraph-marker">§ 1er.</h3><div class="paragraph-content"><p class="intro-text">Pour l'application du présent article, on entend par:</p><ol class="numbered-provisions"><li class="provision" data-number="1°"><span class="provision-text">conversion: la conversion d'instruments financiers inscrits sur un compte-titres en instruments financiers qui ne sont pas inscrits sur un tel compte,<span class="footnote-ref" data-footnote-id="1" data-referenced-text="§ 1er. Pour l'application du présent article, on entend par: 1° conversion: la conversion d'instruments financiers inscrits sur un compte-titres en instruments financiers qui ne sont pas inscrits sur un tel compte, et les autres caractéristiques des instruments financiers restent inchangées, pour autant qu'immédiatement avant cette conversion, la valeur totale des instruments financiers imposables sur le compte concerné soit supérieure à 1.000.000 d'euros; 2° transfert: le transfert, vers un ou plusieurs comptes-titres, d'une partie des instruments financiers imposables inscrits sur un compte-titres sur lequel, immédiatement avant ce transfert, étaient inscrits de tels instruments pour une valeur supérieure à 1.000.000 d'euros, pour autant: a) que le titulaire des comptes concernés soit le même; ou b) que le titulaire du compte au départ duquel a lieu le transfert soit cotitulaire du compte vers lequel le transfert a lieu. Au plus tard le dernier jour du mois qui suit la fin d'une période de référence, l'intermédiaire belge ou le représentant responsable informe l'administration en charge de l'établissement des taxes établies par le Livre II de toute conversion et de tout transfert visés à l'alinéa 1er, 1° et 2°, intervenus pendant cette période de référence. Lorsqu'il s'agit d'un compte-titres détenu à l'étranger et pour lequel aucun représentant responsable n'est désigné, l'obligation d'information à l'administration visée à l'alinéa 2, incombe au titulaire du compte. Est punie d'une amende allant de 250 à 2.500 euros, selon une échelle dont les graduations sont déterminées par le Roi, l'absence de l'information visée à l'alinéa 2 et 3 ainsi qu'une information tardive, inexacte ou incomplète. En l'absence de mauvaise foi, il n'est pas dû d'amende. § 2. Pour l'application de la présente taxe et en vue d'un prélèvement conforme à l'objectif de la loi, la conversion et le transfert ne sont, dans le chef du titulaire, pas opposables à l'administration sauf si le titulaire prouve qu'ils se justifient principalement par un motif autre que la volonté d'éviter la taxe. Le titulaire est redevable de la taxe déduction faite du montant que l'intermédiaire belge ou le représentant responsable est tenu de retenir, déclarer et payer. Les dispositions de l'article 201/9/3 s'appliquent au titulaire visé à l'alinéa 2. § 3. Le Roi détermine les modalités des obligations d'information visées au paragraphe 1er. Le Roi peut en particulier prescrire, le cas échéant, la mention du numéro d'identification d'une personne physique dans le Registre national des personnes physiques ou dans les registres de la Banque Carrefour de la sécurité sociale, lorsque cette personne physique est titulaire ou cotitulaire d'un compte-titres impliqué dans une conversion ou un transfert." data-direct-article-url="https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2025071806#Art.63" data-article-dossier-number="">et les autres caractéristiques des instruments financiers restent inchangées</span>, pour autant qu'immédiatement avant cette conversion, la valeur totale des instruments financiers imposables sur le compte concerné soit supérieure à 1.000.000 d'euros</span></li><li class="provision" data-number="2°"><span class="provision-text">transfert: le transfert, vers un ou plusieurs comptes-titres,<span class="footnote-ref" data-footnote-id="1" data-referenced-text="§ 1er. Pour l'application du présent article, on entend par: 1° conversion: la conversion d'instruments financiers inscrits sur un compte-titres en instruments financiers qui ne sont pas inscrits sur un tel compte, et les autres caractéristiques des instruments financiers restent inchangées, pour autant qu'immédiatement avant cette conversion, la valeur totale des instruments financiers imposables sur le compte concerné soit supérieure à 1.000.000 d'euros; 2° transfert: le transfert, vers un ou plusieurs comptes-titres, d'une partie des instruments financiers imposables inscrits sur un compte-titres sur lequel, immédiatement avant ce transfert, étaient inscrits de tels instruments pour une valeur supérieure à 1.000.000 d'euros, pour autant: a) que le titulaire des comptes concernés soit le même; ou b) que le titulaire du compte au départ duquel a lieu le transfert soit cotitulaire du compte vers lequel le transfert a lieu. Au plus tard le dernier jour du mois qui suit la fin d'une période de référence, l'intermédiaire belge ou le représentant responsable informe l'administration en charge de l'établissement des taxes établies par le Livre II de toute conversion et de tout transfert visés à l'alinéa 1er, 1° et 2°, intervenus pendant cette période de référence. Lorsqu'il s'agit d'un compte-titres détenu à l'étranger et pour lequel aucun représentant responsable n'est désigné, l'obligation d'information à l'administration visée à l'alinéa 2, incombe au titulaire du compte. Est punie d'une amende allant de 250 à 2.500 euros, selon une échelle dont les graduations sont déterminées par le Roi, l'absence de l'information visée à l'alinéa 2 et 3 ainsi qu'une information tardive, inexacte ou incomplète. En l'absence de mauvaise foi, il n'est pas dû d'amende. § 2. Pour l'application de la présente taxe et en vue d'un prélèvement conforme à l'objectif de la loi, la conversion et le transfert ne sont, dans le chef du titulaire, pas opposables à l'administration sauf si le titulaire prouve qu'ils se justifient principalement par un motif autre que la volonté d'éviter la taxe. Le titulaire est redevable de la taxe déduction faite du montant que l'intermédiaire belge ou le représentant responsable est tenu de retenir, déclarer et payer. Les dispositions de l'article 201/9/3 s'appliquent au titulaire visé à l'alinéa 2. § 3. Le Roi détermine les modalités des obligations d'information visées au paragraphe 1er. Le Roi peut en particulier prescrire, le cas échéant, la mention du numéro d'identification d'une personne physique dans le Registre national des personnes physiques ou dans les registres de la Banque Carrefour de la sécurité sociale, lorsque cette personne physique est titulaire ou cotitulaire d'un compte-titres impliqué dans une conversion ou un transfert." data-direct-article-url="https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2025071806#Art.63" data-article-dossier-number="">d'une partie des instruments financiers imposables inscrits sur un compte-titres sur lequel</span>, immédiatement avant ce transfert, étaient inscrits de tels instruments pour une valeur supérieure à 1.000.000 d'euros, pour autant:</span></li></ol><p class="intro-text">a) que le titulaire des comptes concernés soit le même; ou b) que le titulaire du compte au départ duquel a lieu le transfert soit cotitulaire du compte vers lequel le transfert a lieu. Au plus tard le dernier jour du mois qui suit la fin d'une période de référence,<span class="footnote-ref" data-footnote-id="1" data-referenced-text="§ 1er. Pour l'application du présent article, on entend par: 1° conversion: la conversion d'instruments financiers inscrits sur un compte-titres en instruments financiers qui ne sont pas inscrits sur un tel compte, et les autres caractéristiques des instruments financiers restent inchangées, pour autant qu'immédiatement avant cette conversion, la valeur totale des instruments financiers imposables sur le compte concerné soit supérieure à 1.000.000 d'euros; 2° transfert: le transfert, vers un ou plusieurs comptes-titres, d'une partie des instruments financiers imposables inscrits sur un compte-titres sur lequel, immédiatement avant ce transfert, étaient inscrits de tels instruments pour une valeur supérieure à 1.000.000 d'euros, pour autant: a) que le titulaire des comptes concernés soit le même; ou b) que le titulaire du compte au départ duquel a lieu le transfert soit cotitulaire du compte vers lequel le transfert a lieu. Au plus tard le dernier jour du mois qui suit la fin d'une période de référence, l'intermédiaire belge ou le représentant responsable informe l'administration en charge de l'établissement des taxes établies par le Livre II de toute conversion et de tout transfert visés à l'alinéa 1er, 1° et 2°, intervenus pendant cette période de référence. Lorsqu'il s'agit d'un compte-titres détenu à l'étranger et pour lequel aucun représentant responsable n'est désigné, l'obligation d'information à l'administration visée à l'alinéa 2, incombe au titulaire du compte. Est punie d'une amende allant de 250 à 2.500 euros, selon une échelle dont les graduations sont déterminées par le Roi, l'absence de l'information visée à l'alinéa 2 et 3 ainsi qu'une information tardive, inexacte ou incomplète. En l'absence de mauvaise foi, il n'est pas dû d'amende. § 2. Pour l'application de la présente taxe et en vue d'un prélèvement conforme à l'objectif de la loi, la conversion et le transfert ne sont, dans le chef du titulaire, pas opposables à l'administration sauf si le titulaire prouve qu'ils se justifient principalement par un motif autre que la volonté d'éviter la taxe. Le titulaire est redevable de la taxe déduction faite du montant que l'intermédiaire belge ou le représentant responsable est tenu de retenir, déclarer et payer. Les dispositions de l'article 201/9/3 s'appliquent au titulaire visé à l'alinéa 2. § 3. Le Roi détermine les modalités des obligations d'information visées au paragraphe 1er. Le Roi peut en particulier prescrire, le cas échéant, la mention du numéro d'identification d'une personne physique dans le Registre national des personnes physiques ou dans les registres de la Banque Carrefour de la sécurité sociale, lorsque cette personne physique est titulaire ou cotitulaire d'un compte-titres impliqué dans une conversion ou un transfert." data-direct-article-url="https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2025071806#Art.63" data-article-dossier-number="">l'intermédiaire belge ou le représentant responsable informe l'administration en charge de l'établissement des taxes établies par le Livre II de toute conversion et de tout transfert visés à l'alinéa 1er</span>,:</p><ol class="numbered-provisions"><li class="provision" data-number="1°"><span class="provision-text">et</span></li></ol><p class="closing-text">2°, intervenus pendant cette période de référence. Lorsqu'il s'agit d'un compte-titres détenu à l'étranger et pour lequel aucun représentant responsable n'est désigné, l'obligation d'information à l'administration visée à l'alinéa 2, incombe au titulaire du compte. Est punie d'une amende allant de 250 à 2.500 euros, selon une échelle dont les graduations sont déterminées par le Roi, l'absence de l'information visée à l'alinéa 2 et 3 ainsi qu'une information tardive, inexacte ou incomplète. En l'absence de mauvaise foi, il n'est pas dû d'amende.</p></div></section><section class="paragraph" id="para-2"><h3 class="paragraph-marker">§ 2.</h3><div class="paragraph-content"><p><span class="footnote-ref" data-footnote-id="1" data-referenced-text="§ 1er. Pour l'application du présent article, on entend par: 1° conversion: la conversion d'instruments financiers inscrits sur un compte-titres en instruments financiers qui ne sont pas inscrits sur un tel compte, et les autres caractéristiques des instruments financiers restent inchangées, pour autant qu'immédiatement avant cette conversion, la valeur totale des instruments financiers imposables sur le compte concerné soit supérieure à 1.000.000 d'euros; 2° transfert: le transfert, vers un ou plusieurs comptes-titres, d'une partie des instruments financiers imposables inscrits sur un compte-titres sur lequel, immédiatement avant ce transfert, étaient inscrits de tels instruments pour une valeur supérieure à 1.000.000 d'euros, pour autant: a) que le titulaire des comptes concernés soit le même; ou b) que le titulaire du compte au départ duquel a lieu le transfert soit cotitulaire du compte vers lequel le transfert a lieu. Au plus tard le dernier jour du mois qui suit la fin d'une période de référence, l'intermédiaire belge ou le représentant responsable informe l'administration en charge de l'établissement des taxes établies par le Livre II de toute conversion et de tout transfert visés à l'alinéa 1er, 1° et 2°, intervenus pendant cette période de référence. Lorsqu'il s'agit d'un compte-titres détenu à l'étranger et pour lequel aucun représentant responsable n'est désigné, l'obligation d'information à l'administration visée à l'alinéa 2, incombe au titulaire du compte. Est punie d'une amende allant de 250 à 2.500 euros, selon une échelle dont les graduations sont déterminées par le Roi, l'absence de l'information visée à l'alinéa 2 et 3 ainsi qu'une information tardive, inexacte ou incomplète. En l'absence de mauvaise foi, il n'est pas dû d'amende. § 2. Pour l'application de la présente taxe et en vue d'un prélèvement conforme à l'objectif de la loi, la conversion et le transfert ne sont, dans le chef du titulaire, pas opposables à l'administration sauf si le titulaire prouve qu'ils se justifient principalement par un motif autre que la volonté d'éviter la taxe. Le titulaire est redevable de la taxe déduction faite du montant que l'intermédiaire belge ou le représentant responsable est tenu de retenir, déclarer et payer. Les dispositions de l'article 201/9/3 s'appliquent au titulaire visé à l'alinéa 2. § 3. Le Roi détermine les modalités des obligations d'information visées au paragraphe 1er. Le Roi peut en particulier prescrire, le cas échéant, la mention du numéro d'identification d'une personne physique dans le Registre national des personnes physiques ou dans les registres de la Banque Carrefour de la sécurité sociale, lorsque cette personne physique est titulaire ou cotitulaire d'un compte-titres impliqué dans une conversion ou un transfert." data-direct-article-url="https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2025071806#Art.63" data-article-dossier-number="">Pour l'application de la présente taxe et en vue d'un prélèvement conforme à l'objectif de la loi, la conversion et le transfert ne sont, dans le chef du titulaire, pas opposables à l'administration sauf si le titulaire prouve qu'ils se justifient principalement par un motif autre que la volonté d'éviter la taxe</span>. Le titulaire est redevable de la taxe déduction faite du montant que l'intermédiaire belge ou le représentant responsable est tenu de retenir, déclarer et payer. Les dispositions de l'article 201/9/3 s'appliquent au titulaire visé à l'alinéa 2.</p></div></section><section class="paragraph" id="para-3"><h3 class="paragraph-marker">§ 3.</h3><div class="paragraph-content"><p>Le Roi détermine les modalités des obligations d'information visées au paragraphe 1er.<span class="footnote-ref" data-footnote-id="1" data-referenced-text="§ 1er. Pour l'application du présent article, on entend par: 1° conversion: la conversion d'instruments financiers inscrits sur un compte-titres en instruments financiers qui ne sont pas inscrits sur un tel compte, et les autres caractéristiques des instruments financiers restent inchangées, pour autant qu'immédiatement avant cette conversion, la valeur totale des instruments financiers imposables sur le compte concerné soit supérieure à 1.000.000 d'euros; 2° transfert: le transfert, vers un ou plusieurs comptes-titres, d'une partie des instruments financiers imposables inscrits sur un compte-titres sur lequel, immédiatement avant ce transfert, étaient inscrits de tels instruments pour une valeur supérieure à 1.000.000 d'euros, pour autant: a) que le titulaire des comptes concernés soit le même; ou b) que le titulaire du compte au départ duquel a lieu le transfert soit cotitulaire du compte vers lequel le transfert a lieu. Au plus tard le dernier jour du mois qui suit la fin d'une période de référence, l'intermédiaire belge ou le représentant responsable informe l'administration en charge de l'établissement des taxes établies par le Livre II de toute conversion et de tout transfert visés à l'alinéa 1er, 1° et 2°, intervenus pendant cette période de référence. Lorsqu'il s'agit d'un compte-titres détenu à l'étranger et pour lequel aucun représentant responsable n'est désigné, l'obligation d'information à l'administration visée à l'alinéa 2, incombe au titulaire du compte. Est punie d'une amende allant de 250 à 2.500 euros, selon une échelle dont les graduations sont déterminées par le Roi, l'absence de l'information visée à l'alinéa 2 et 3 ainsi qu'une information tardive, inexacte ou incomplète. En l'absence de mauvaise foi, il n'est pas dû d'amende. § 2. Pour l'application de la présente taxe et en vue d'un prélèvement conforme à l'objectif de la loi, la conversion et le transfert ne sont, dans le chef du titulaire, pas opposables à l'administration sauf si le titulaire prouve qu'ils se justifient principalement par un motif autre que la volonté d'éviter la taxe. Le titulaire est redevable de la taxe déduction faite du montant que l'intermédiaire belge ou le représentant responsable est tenu de retenir, déclarer et payer. Les dispositions de l'article 201/9/3 s'appliquent au titulaire visé à l'alinéa 2. § 3. Le Roi détermine les modalités des obligations d'information visées au paragraphe 1er. Le Roi peut en particulier prescrire, le cas échéant, la mention du numéro d'identification d'une personne physique dans le Registre national des personnes physiques ou dans les registres de la Banque Carrefour de la sécurité sociale, lorsque cette personne physique est titulaire ou cotitulaire d'un compte-titres impliqué dans une conversion ou un transfert." data-direct-article-url="https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2025071806#Art.63" data-article-dossier-number="">Le Roi peut en particulier prescrire, le cas échéant, la mention du numéro d'identification d'une personne physique dans le Registre national des personnes physiques ou dans les registres de la Banque Carrefour de la sécurité sociale, lorsque cette personne physique est titulaire ou cotitulaire d'un compte-titres impliqué dans une conversion ou un transfert.</span></p></div></section></div></article>`,
  raw_markdown: `**ARTICLE**[Art.] [201/9/6]. [1 § 1er. Pour l'application du présent article, on entend par:  
1° conversion: la conversion d'instruments financiers inscrits sur un compte-titres en instruments financiers qui ne sont pas inscrits sur un tel compte, et les autres caractéristiques des instruments financiers restent inchangées, pour autant qu'immédiatement avant cette conversion, la valeur totale des instruments financiers imposables sur le compte concerné soit supérieure à 1.000.000 d'euros;  
2° transfert: le transfert, vers un ou plusieurs comptes-titres, d'une partie des instruments financiers imposables inscrits sur un compte-titres sur lequel, immédiatement avant ce transfert, étaient inscrits de tels instruments pour une valeur supérieure à 1.000.000 d'euros, pour autant:  
a) que le titulaire des comptes concernés soit le même; ou  
b) que le titulaire du compte au départ duquel a lieu le transfert soit cotitulaire du compte vers lequel le transfert a lieu.  
Au plus tard le dernier jour du mois qui suit la fin d'une période de référence, l'intermédiaire belge ou le représentant responsable informe l'administration en charge de l'établissement des taxes établies par le Livre II de toute conversion et de tout transfert visés à l'alinéa 1er, 1° et 2°, intervenus pendant cette période de référence.  
Lorsqu'il s'agit d'un compte-titres détenu à l'étranger et pour lequel aucun représentant responsable n'est désigné, l'obligation d'information à l'administration visée à l'alinéa 2, incombe au titulaire du compte.  
Est punie d'une amende allant de 250 à 2.500 euros, selon une échelle dont les graduations sont déterminées par le Roi, l'absence de l'information visée à l'alinéa 2 et 3 ainsi qu'une information tardive, inexacte ou incomplète.  
En l'absence de mauvaise foi, il n'est pas dû d'amende.  
§ 2. Pour l'application de la présente taxe et en vue d'un prélèvement conforme à l'objectif de la loi, la conversion et le transfert ne sont, dans le chef du titulaire, pas opposables à l'administration sauf si le titulaire prouve qu'ils se justifient principalement par un motif autre que la volonté d'éviter la taxe.  
Le titulaire est redevable de la taxe déduction faite du montant que l'intermédiaire belge ou le représentant responsable est tenu de retenir, déclarer et payer.  
Les dispositions de l'article 201/9/3 s'appliquent au titulaire visé à l'alinéa 2.  
§ 3. Le Roi détermine les modalités des obligations d'information visées au paragraphe 1er.  
Le Roi peut en particulier prescrire, le cas échéant, la mention du numéro d'identification d'une personne physique dans le Registre national des personnes physiques ou dans les registres de la Banque Carrefour de la sécurité sociale, lorsque cette personne physique est titulaire ou cotitulaire d'un compte-titres impliqué dans une conversion ou un transfert.]1  
\----------  
(1)<Inséré par L [2025-07-18/06](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2025071806), art. 63, 063; En vigueur : 29-07-2025>`
};

// Additional test cases with problematic HTML
const testCases: { name: string; data: TransformationInput }[] = [
  {
    name: "Well-formed article with footnote",
    data: mockData
  },
  {
    name: "Article with broken HTML and numbered list",
    data: {
      document_number: "TEST001",
      article_number: "42",
      main_text: `<div>Article 42<p>Les conditions sont:</p>1° avoir 18 ans<br>2° être domicilié<span class="footnote-ref" data-footnote-id="2" data-referenced-text="en Belgique" data-direct-article-url="http://example.com">en Belgique</span><br>3° avoir la nationalité</div>`,
      raw_markdown: "Article 42 Les conditions sont: 1° avoir 18 ans 2° être domicilié en Belgique 3° avoir la nationalité"
    }
  }
];

async function runTests() {
  console.log('🧪 Starting HTML Transformation Tests with Gemini 2.5 Flash\n');
  console.log('=' .repeat(70));

  // Check if API key is configured
  const googleApiKey = process.env.GOOGLE_API_KEY || process.env.GEMINI_API_KEY;
  if (!googleApiKey || googleApiKey === 'YOUR_GOOGLE_API_KEY_HERE') {
    console.error('❌ ERROR: GOOGLE_API_KEY/GEMINI_API_KEY not configured in .env file');
    console.log('\nPlease set your GOOGLE_API_KEY or GEMINI_API_KEY in the .env file to run tests.');
    process.exit(1);
  }

  let successCount = 0;
  let failureCount = 0;
  let skippedCount = 0;
  const testResults: any[] = [];

  for (const testCase of testCases) {
    console.log(`\n📋 Test: ${testCase.name}`);
    console.log('-'.repeat(50));
    console.log(`Document: ${testCase.data.document_number}`);
    console.log(`Article: ${testCase.data.article_number}`);
    console.log(`Input HTML length: ${testCase.data.main_text.length} chars`);
    console.log(`Raw markdown length: ${testCase.data.raw_markdown.length} chars`);
    
    const startTime = Date.now();
    
    try {
      const result = await transformArticleHtml(testCase.data);
      const duration = Date.now() - startTime;
      
      // Prepare test result object
      const testResult: any = {
        testName: testCase.name,
        document_number: testCase.data.document_number,
        article_number: testCase.data.article_number,
        inputHtmlLength: testCase.data.main_text.length,
        rawMarkdownLength: testCase.data.raw_markdown.length,
        duration_ms: duration,
        timestamp: new Date().toISOString()
      };
      
      if (result.skipped) {
        skippedCount++;
        console.log(`⏭️ SKIPPED - ${result.skipReason} (${duration}ms)`);
        
        testResult.success = true;
        testResult.skipped = true;
        testResult.skipReason = result.skipReason;
        
      } else if (result.success && result.transformedHtml) {
        successCount++;
        console.log(`✅ SUCCESS - Transformation completed in ${duration}ms`);
        console.log(`Output HTML length: ${result.transformedHtml.length} chars`);
        
        // Validate key requirements
        const validations = [];
        const validationResults: any = {};
        
        // Check for legal-article class
        const hasLegalArticleClass = result.transformedHtml.includes('class="legal-article"');
        validationResults.hasLegalArticleClass = hasLegalArticleClass;
        if (hasLegalArticleClass) {
          validations.push('✓ Contains legal-article class');
        } else {
          validations.push('✗ Missing legal-article class');
        }
        
        // Check for article number
        const hasArticleNumber = result.transformedHtml.includes(testCase.data.article_number);
        validationResults.hasArticleNumber = hasArticleNumber;
        if (hasArticleNumber) {
          validations.push('✓ Contains article number');
        } else {
          validations.push('✗ Missing article number');
        }
        
        // Check footnote preservation
        const inputFootnotes = (testCase.data.main_text.match(/data-footnote-id="[^"]+"/g) || []).length;
        const outputFootnotes = (result.transformedHtml.match(/data-footnote-id="[^"]+"/g) || []).length;
        validationResults.inputFootnotes = inputFootnotes;
        validationResults.outputFootnotes = outputFootnotes;
        validationResults.footnotesPreserved = inputFootnotes === outputFootnotes;
        
        if (inputFootnotes === outputFootnotes) {
          validations.push(`✓ All ${inputFootnotes} footnote(s) preserved`);
        } else {
          validations.push(`✗ Footnote mismatch: ${inputFootnotes} input, ${outputFootnotes} output`);
        }
        
        console.log('\nValidation checks:');
        validations.forEach(v => console.log(`  ${v}`));
        
        // Show a snippet of the transformed HTML
        console.log('\nTransformed HTML (first 300 chars):');
        console.log(result.transformedHtml.substring(0, 300) + '...');
        
        // Add to test result
        testResult.success = true;
        testResult.outputHtmlLength = result.transformedHtml.length;
        testResult.validations = validationResults;
        testResult.originalHtml = testCase.data.main_text;
        testResult.transformedHtml = result.transformedHtml;
        testResult.model = 'gemini-2.5-flash';
        
        console.log(`🤖 Model used: Gemini 2.5 Flash`);
        
      } else {
        failureCount++;
        console.log(`❌ FAILURE - Transformation failed after ${duration}ms`);
        
        if (result.error) {
          console.log(`Error: ${result.error}`);
        }
        
        if (result.validationErrors && result.validationErrors.length > 0) {
          console.log('Validation errors:');
          result.validationErrors.forEach(err => console.log(`  - ${err}`));
        }
        
        if (result.transformedHtml) {
          console.log('\nPartial output (first 300 chars):');
          console.log(result.transformedHtml.substring(0, 300) + '...');
        }
        
        console.log(`🤖 Model used: Gemini 2.5 Flash`);
        
        // Add failure to test result
        testResult.success = false;
        testResult.error = result.error;
        testResult.validationErrors = result.validationErrors;
        testResult.originalHtml = testCase.data.main_text;
        testResult.partialOutput = result.transformedHtml;
        testResult.model = 'gemini-2.5-flash';
      }
      
      testResults.push(testResult);
      
    } catch (error: any) {
      failureCount++;
      const duration = Date.now() - startTime;
      console.log(`❌ EXCEPTION - Test failed after ${duration}ms`);
      console.log(`Error: ${error.message}`);
      console.log(`Stack: ${error.stack}`);
      
      // Add exception to test results
      testResults.push({
        testName: testCase.name,
        document_number: testCase.data.document_number,
        article_number: testCase.data.article_number,
        success: false,
        duration_ms: duration,
        exception: true,
        error: error.message,
        stack: error.stack,
        timestamp: new Date().toISOString()
      });
    }
  }
  
  // Final summary
  console.log('\n' + '='.repeat(70));
  console.log('📊 TEST SUMMARY');
  console.log('='.repeat(70));
  console.log(`Total tests: ${testCases.length}`);
  console.log(`✅ Passed: ${successCount}`);
  console.log(`⏭️ Skipped: ${skippedCount}`);
  console.log(`❌ Failed: ${failureCount}`);
  const totalProcessed = successCount + skippedCount;
  console.log(`Success rate: ${((totalProcessed / testCases.length) * 100).toFixed(1)}%`);
  
  // Save test results to JSON file
  const testSummary = {
    summary: {
      totalTests: testCases.length,
      passed: successCount,
      skipped: skippedCount,
      failed: failureCount,
      successRate: ((totalProcessed / testCases.length) * 100).toFixed(1) + '%',
      model: 'gemini-2.5-flash',
      timestamp: new Date().toISOString()
    },
    testResults: testResults
  };
  
  const outputDir = path.join(__dirname, 'test-results');
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
  }
  
  const timestamp = new Date().toISOString().replace(/[:.]/g, '-').slice(0, -5);
  const outputFile = path.join(outputDir, `test-results-${timestamp}.json`);
  
  fs.writeFileSync(outputFile, JSON.stringify(testSummary, null, 2));
  console.log(`\n💾 Test results saved to: ${outputFile}`);
  
  if (failureCount === 0) {
    console.log('\n🎉 All tests passed successfully!');
  } else {
    console.log('\n⚠️ Some tests failed. Please review the errors above.');
  }
  
  process.exit(failureCount > 0 ? 1 : 0);
}

// Run tests if this file is executed directly
if (require.main === module) {
  runTests().catch(error => {
    console.error('Fatal error running tests:', error);
    process.exit(1);
  });
}

export { runTests };