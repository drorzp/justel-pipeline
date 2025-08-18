import mongoose, { Types, Document } from 'mongoose';

export interface IDecisionForArticleDetail {
  file_name: string;
  url_official_publication: string;
  ecli_alias: string;
  language_metadata: string;
  court_ecli_code: string;
  court_fr: string;
  court_category: string;
  decision_type_fr: string;
  decision_type_ecli_code: string;
  decision_date: string;
  decision_year: string;
  versions: string;
  url_pdf: string;
  ecli: string;
}

export interface IDecisionForArticle {
  decision_article_id: number;
  decision_id: string;
  summary_id: string;
  edge: string;
  legal_act_type: string;
  url_text: string;
  url_justel: string;
  law_document_id: string;
  article_link_number: string;
  decision_article_created_at: Date;
  decision_details: IDecisionForArticleDetail;
}
export interface IFootNotes {
  id: number;
  footnote_number: string;
  footnote_content: string;
  law_type: string;
  date_reference: string;
  sequence_number: string;
  full_reference: string;
  effective_date: string;
  modification_type: string;
  direct_url: string;
  direct_article_url: string;
  created_at: Date;
}
export interface IFootNotesRef {
  id: number;
  footnote_id: number;
  reference_number: string;
  text_position: string;
  referenced_text: string;
  bracket_pattern: string;
  created_at: Date;
}

export interface IArticle extends Document {
  id: number;
  hierarchy_element_id: number;
  article_number: string;
  document_number: string;
  anchor_id: string;
  main_text: string;

  created_at: Date;
  // footnotes:IFootNotes[];
  // footnote_references:IFootNotesRef[];
  decisions: IDecisionForArticle[];
}

// Note interface
export interface INote extends Document {
  userId: string;
  decisionId: string;
  note: string;
  createdAt: Date;
  updatedAt: Date;
}

interface Keyword {
  keywords_sequence_fr_new: string;
}

interface DecisionKeywords {
  keywords: Keyword[];
  matched_decisions_id: string;
}

export interface ISimilarKeywords {
  [decisionId: string]: DecisionKeywords;
}

export interface IDecisionSummaryItem {
  summary_id: string;
  text: string;
  rank?: number;
}

export interface IsimilairArticle {
  id: number;
  summary_id: string;
  edge: string;
  legal_act_type: string;
  article_number: string;
  url_text: string;
  url_justel: string;
  law_document_id: string;
  created_at: Date;
  article_link_number: string;
}

export interface Isimilair {
  id: number;
  source_decisions_id: string;
  matched_decisions_id: string;
  articles: IsimilairArticle[];
  keywords: string;
  grade: number;
  matched_decision_details: {
    court_fr: string;
    decision_date: string;
    decision_type_fr: string;
    decision_id: string;
  };
}

export interface KeywordList {
  id: number;
  keyword_id: string;
  keywords_sequence_fr_new: string;
  level: string;
  parent?: string;
  summary?: string;
}

export interface IkeywordRequest {
  keyword: string;
  code: string;
}

export type Summary = {
  id: string;
  text: string;
};

export type Article = {
  id: string;
  text: string;
};

export type RerankedResult = {
  id: string;
  score: number;
};

export interface IkeywordSummary {
  code: string;
  keyword: string;
  summary?: string;
}

export interface IDecisionSummary {
  text: string;
  pdf: string;
  decision: string;
  publication?: string;
  ecli?: string;
  language: string;
  court: string;
  decision_type: string;
  decision_date: string;
  decision_year: string;
  versions?: string;
  court_ecli_code: string;
  court_category: string;
  keywords: string[];
}

export interface IDecision {
  decisionId: string;
  decision_ecli: string;
  file_name: string;
  url_official_publication: string | null;
  ecli_alias: string | null;
  language_metadata: string;
  court_ecli_code: string | null;
  court_fr: string | null;
  court_category: string | null;
  decision_type_fr: string | null;
  decision_type_ecli_code: string | null;
  decision_date: string | null;
  decision_year: string | null;
  versions: string | null;
  url_pdf: string | null;
  keywords: string[];
  similarKeywords: ISimilarKeywords;
  similairs: Isimilair[];
  summaries: IDecisionSummaryItem[];
  fulltext: string | null;
  articleOfLaw: IArticleOfLaw[] | null;
  // Virtual fields
  notes?: INote[];
  folders?: ILawyerfolder[];
}
export interface IDecisionRoot {
  decision_id: string;
  decision_ecli: string;
  file_name: string;
  url_official_publication: string | null;
  ecli: string | null;
  language_metadata: string;
  court_ecli_code: string | null;
  court_fr: string | null;
  court_category: string | null;
  decision_type_fr: string | null;
  decision_type_ecli_code: string | null;
  decision_date: string | null;
  decision_year: string | null;
  versions: string | null;
  url_pdf: string | null;
  keywords: string[];
  similar_keywords: ISimilarKeywords;
  similair: Isimilair[];
  summaries: IDecisionSummaryItem[];
  fulltext: string | null;
  articles: IArticleOfLaw[] | null;
  // Virtual fields
  notes?: INote[];
  folders?: ILawyerfolder[];
}

export interface IArticleOfLaw {
  id: number;
  decision_id: string;
  law_document_id: string;
  article_number: string;
  article_link_number: string;
  legal_act_type: string;
  article_title?: string;
  content?: string;
  title?: string;
  publication_date?: Date;
  source?: string;
  page_number?: number;
  dossier_number?: string;
  effective_date?: Date;
  language?: string;
  document_type?: string;
  status?: string;
}

// Document Comparison Types
export interface DocumentMetadata {
  fileName: string;
  fileSize: number;
  fileType: string;
  lastModified?: number;
  extractedText: string;
  processingTime: number;
}

export interface DiffChange {
  type: 'added' | 'removed' | 'unchanged';
  value: string;
  count?: number;
  lineNumber?: number;
}

export interface ComparisonSummary {
  totalChanges: number;
  addedCount: number;
  removedCount: number;
  unchangedCount: number;
  addedWords: number;
  removedWords: number;
  unchangedWords: number;
}

export interface DocumentComparisonResult {
  success: boolean;
  oldDocument: DocumentMetadata;
  newDocument: DocumentMetadata;
  differences: DiffChange[];
  summary: ComparisonSummary;
  hasChanges: boolean;
  processingTime: number;
  timestamp: string;
}

export interface DocumentComparisonError {
  success: false;
  error: {
    code: string;
    message: string;
    details?: string;
  };
  timestamp: string;
}

export interface ILawyerfolder extends Document {
  userId: string;
  folderName: string;
  folderDescription: string;
  decisionIds: string[];
  createdAt: Date;
  updatedAt: Date;
  getDisplayName(): string;
  formattedCreatedAt: string; // Add virtual property to interface
}

export type IHistorySummary = {
  id: string;
  text: String;
  rank?: number;
};

export interface IHistoryDecision {
  _decisionId: string;
  decisionId: string;
  decision_ecli: string;
  file_name: string;
  url_official_publication: string | null;
  ecli_alias: string | null;
  language_metadata: string;
  court_ecli_code: string | null;
  court_fr: string | null;
  court_category: string | null;
  decision_date: string | null;
  decision_type_fr: string | null;
  rank: number;
  keywords: string[];
  summaries: IHistorySummary[];
}
export interface ISimilairVectorArticle {
  law_id: string;
  article_number: string;
  title: string;
  score: number;
}
export interface IHistory extends Document {
  _id: Types.ObjectId;
  userId: string;
  prompt: string;
  decisions: IHistoryDecision[];
  similairArticles: ISimilairVectorArticle[];
  folders?: ILawyerfolder[];
  createdAt: Date;
  formattedCreatedAt: string; // virtual field
  notes?: any[]; // virtual field for user's notes on decisions in this history
  fullDecisions?: any[]; // virtual field for populated Decision documents
  decisionCount: number; // virtual field for decision count
  uniqueCourts: string[]; // virtual field for unique courts
  totalSummariesCount: number; // virtual field for total summaries count
}

export interface IApiLog extends Document {
  userEmail: string | null;
  prompt: string;
  response1: string;
  response2: string;
  decisions: any[];
  createdAt: Date;
}

export interface IUser extends Document {
  email: string;
  name: string;
  createdAt: Date;
  updatedAt: Date;
  getDisplayName(): string; // Add method to interface for better typing
}

export interface ISimilairArticle extends Document {
  id: Number;
  summary_id: string;
  decision_id: string;
  edge: string;
  legal_act_type: string;
  article_number: string;
  url_text: string;
  url_justel: string;
  law_document_id: string;
  created_at: Date;
  article_link_number: string;
}

export interface IExtraction_metadata extends Document {
  id: number;
  document_id: string;
  extraction_date: Date;
  source_file: string;
  sections_included: string[];
  sections_excluded: string[];
  all_articles_extracted: boolean;
  footnotes_linked: boolean;
  hierarchical_structure_complete: boolean;
  metadata_complete: boolean;
  is_minimal_document: boolean;
  created_at: Date;
}

export interface IDocument_modifies extends Document {
  id: number;
  document_id: string;
  modified_document_number: string;
  modified_document_title: string;
  modification_type: string;
  modification_date: Date;
  created_at: Date;
}

export interface IDocument_version extends Document {
  id: number;
  document_id: string;
  archived_versions_count: number;
  archived_versions_url: string | null;
  execution_orders_count: number;
  execution_orders_url: string | null;
  created_at: Date;
}
export interface IExternal_link extends Document {
  id: number;
  document_id: string;
  link_type: string;
  link_url: string;
  link_title: string;
  link_description: string;
  order_index: number;
  created_at: Date;
}

export interface IHierarchy_element extends Document {
  id: number;
  document_id: string;
  parent_id: number;
  element_type: string;
  label: string;
  title_type: string;
  title_content: string;
  article_range: string;
  rank: number;
  level: number;
  path: string;
  created_at: Date;
}

export interface ILaw extends Document {
  id: number;
  document_number: string;
  title: string;
  publication_date: string | null;
  source: string;
  page_number: number;
  dossier_number: string | null;
  effective_date: string | null;
  language: string | null;
  document_type: string | null;
  status: string | null;
  official_justel_url: string | null;
  official_publication_pdf_url: string | null;
  consolidated_pdf_url: string | null;
  document_modifies: IDocument_modifies[];
  document_versions: IDocument_version[];
  external_links: IExternal_link[];
  hierarchy_elements: IHierarchy_element[];
  extraction_metadata: IExtraction_metadata;
  selectedArticle?: IArticle;
  created_at: Date;
  updated_at: Date;
}
