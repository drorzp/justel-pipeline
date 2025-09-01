import mongoose, { Document, Schema } from 'mongoose';
import { IArticle } from './types';

// Schema for decision details within articles
const DecisionForArticleDetailSchema = new Schema({
  file_name: { type: String, required: true },
  url_official_publication: { type: String, required: true },
  ecli_alias: { type: String, default: null },
  language_metadata: { type: String, required: true },
  court_ecli_code: { type: String, required: true },
  court_fr: { type: String, required: true },
  court_category: { type: String, required: true },
  decision_type_fr: { type: String, required: true },
  decision_type_ecli_code: { type: String, required: true },
  decision_date: { type: String, required: true },
  decision_year: { type: String, required: true },
  versions: { type: String, default: null },
  url_pdf: { type: String, default: null },
  ecli: { type: String, default: null }
}, { _id: false });

// Schema for decisions within articles
const DecisionForArticleSchema = new Schema({
  decision_article_id: { type: Number, required: true },
  decision_id: { type: String, required: true },
  summary_id: { type: String, required: true },
  edge: { type: String, required: true },
  legal_act_type: { type: String, required: true },
  url_text: { type: String, required: true },
  url_justel: { type: String, required: true },
  law_document_id: { type: String, required: true },
  article_link_number: { type: String, required: true },
  decision_article_created_at: { type: Date, required: true },
  decision_details: { type: DecisionForArticleDetailSchema, required: true }
}, { _id: false });

// Main Article schema
export const ArticleSchema = new Schema<IArticle>({
  id: { type: Number, required: true, unique: true },
  hierarchy_element_id: { type: Number, required: true },
  article_number: { type: String, required: true },
  document_number: { type: String, required: true },
  anchor_id: { type: String, required: true },
  main_text: { type: String, required: true },
  created_at: { type: Date, required: true },
  decisions: { type: [DecisionForArticleSchema], default: [] }
}, {
  timestamps: true,
  versionKey: false,
  toJSON: { virtuals: true },
  toObject: { virtuals: true },
});

// Create compound unique index for article_number and document_number
ArticleSchema.index({ article_number: 1, document_number: 1 }, { unique: true });

const Article = mongoose.model<IArticle>('articles', ArticleSchema);
export { Article };