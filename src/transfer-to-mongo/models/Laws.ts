import mongoose, { Schema } from 'mongoose';
import {
  ICiting_decisions,
  IDocument_modifies,
  IDocument_version,
  IExternal_link,
  IExtraction_metadata,
  IHierarchy_element,
  ILaw,
} from './types';
import { ArticleSchema } from './Articles.js';

const document_citing_decisions = new Schema<ICiting_decisions>({
  decision_id: { type: Number},
  pg_id:{type:Number},
  ecli: {type:String},
  file_name: { type: String ,default: null},
  url_official_publication: { type: String  ,default: null},
  language_metadata: { type: String  ,default: null},
  court_ecli_code: { type: String  ,default: null},
  decision_type_ecli_code: { type: String ,default: null },
  decision_date: { type: String  ,default: null},
  url_pdf: { type: String, default: null },
  rol_number: { type: String, default: null },
  case: { type: String, default: null },
  chamber: { type: String, default: null },
  field_of_law: { type: String, default: null },
  opinion_public_attorney: { type: String, default: null },
  source: { type: String  ,default: null},
  court_fr: { type: String ,default: null },
  court_nl: { type: String  ,default: null},
  court_category: { type: String  ,default: null},
  decision_type_fr: { type: String  ,default: null},
  decision_type_nl: { type: String  ,default: null},
  micro_summary: { type: String, default: null },
  citation_reference: { type: String, default: null },
  facts: { type: String, default: null },
  court_order: { type: String, default: null },
  outcome: { type: String, default: null },
  keywords: { type: [String], default: [] },
  sorted_court: { type: Number,  default: null},
  cited_articles: { type: [String] },

}, { _id: false });



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
      citing_decisions: {type:[document_citing_decisions],default:[]}
      // selectedArticle?:{type: ArticleSchema}
  },
  {
    timestamps: true,
    versionKey: false,
    toJSON: { virtuals: true },
    toObject: { virtuals: true },
  }
);

RootLawSchema.index({ 'document.document_number': 1 }, { unique: false });

const Law = mongoose.model<ILaw>('law', RootLawSchema);

export { Law };
export type { ILaw };
