import mongoose, { Schema } from 'mongoose';
import {
  IDocument_modifies,
  IDocument_version,
  IExternal_link,
  IExtraction_metadata,
  IHierarchy_element,
  ILaw,
} from './types';
import { ArticleSchema } from './Articles.js';

const document_versionsSchema = new Schema<IDocument_version>({
  id: { type: Number, required: true },
  document_id: { type: String, required: true },
  archived_versions_count: { type: Number },
  archived_versions_url: { type: String },
  execution_orders_count: { type: Number },
  execution_orders_url: { type: String },
  created_at: { type: Date },
});
const document_modifiesSchema = new Schema<IDocument_modifies>({
  id: { type: Number, required: true },
  document_id: { type: String, required: true },
  modified_document_number: { type: String },
  modified_document_title: { type: String },
  modification_type: { type: String },
  modification_date: { type: Date },
  created_at: { type: Date },
});

const external_linksSchema = new Schema<IExternal_link>({
  id: { type: Number, required: true },
  document_id: { type: String, required: true },
  link_type: { type: String },
  link_url: { type: String },
  link_title: { type: String },
  link_description: { type: String },
  order_index: { type: Number },
  created_at: { type: Date },
});

const hierarchy_elementsSchema = new Schema<IHierarchy_element>({
  id: { type: Number, required: true },
  document_id: { type: String, required: true },
  parent_id: { type: Number },
  element_type: { type: String },
  label: { type: String },
  title_type: { type: String },
  title_content: { type: String },
  article_range: { type: String },
  rank: { type: Number },
  level: { type: Number },
  path: { type: String },
  created_at: { type: Date },
});

const extraction_metadataSchema = new Schema<IExtraction_metadata>({
  id: { type: Number, required: true },
  document_id: { type: String, required: true },
  extraction_date: { type: Date },
  source_file: { type: String },
  sections_included: { type: [String] },
  sections_excluded: { type: [String] },
  all_articles_extracted: { type: Boolean },
  footnotes_linked: { type: Boolean },
  hierarchical_structure_complete: { type: Boolean },
  metadata_complete: { type: Boolean },
  is_minimal_document: { type: Boolean },
  created_at: { type: Date },
});

const RootLawSchema = new Schema<ILaw>(
  {
      id: { type: Number, required: true },
      document_number: { type: String, required: true },
      title: { type: String },
      publication_date: { type: String },
      source: { type: String },
      page_number: { type: Number },
      dossier_number: { type: String },
      effective_date: { type: String },
      language: { type: String },
      document_type: { type: String },
      status: { type: String },
      official_justel_url: { type: String },
      official_publication_pdf_url: { type: String },
      consolidated_pdf_url: { type: String },
      created_at: { type: Date },
      updated_at: { type: Date },
      document_modifies: { type: [document_modifiesSchema], default: [] },
      document_versions: { type: [document_versionsSchema], default: [] },
      external_links: { type: [external_linksSchema], default: [] },
      hierarchy_elements: { type: [hierarchy_elementsSchema], default: [] },
      extraction_metadata: { type: extraction_metadataSchema },
      // selectedArticle?:{type: ArticleSchema}
  },
  {
    timestamps: true,
    versionKey: false,
    toJSON: { virtuals: true },
    toObject: { virtuals: true },
  }
);

RootLawSchema.index({ 'document.document_number': 1 }, { unique: true });

const LawRoot = mongoose.model<ILaw>('lawroots', RootLawSchema);

export { LawRoot };
export type { ILaw };
