import mongoose, { Document, Schema } from 'mongoose';
import { IArticle } from './types';

// Schema for decisions within articles
const DecisionForArticleSchema = new Schema({
  decision_article_id: { type: Number, required: true },
  decision_id: { type: String, required: true },
  decision_date:{type:String},
  keywords:{type:[String]},
  court:{type:String},
  sorted_court:{type:Number},
  block_ids:{type:[String]},
  relevant_snippet:{type:[String]},
  relevant_factual_context:{type:String},
  rol_number:{type:String}, 
  provision_interpretation:{type:String},
  legal_act_type: { type: String, required: true },
  law_document_id: { type: String, required: true },
  article_link_number: { type: String, required: true },
  decision_article_created_at: { type: Date, required: true },
  url_official_publication: { type: String, required: true },
  ecli_alias: { type: String, default: null },
  language_metadata: { type: String, required: true },
  court_ecli_code: { type: String, required: true },
  court_fr: { type: String, required: true },
  court_category: { type: String, required: true },
  decision_type_fr: { type: String, required: true },
  decision_type_ecli_code: { type: String, required: true },
  decision_year: { type: String, required: true },
  versions: {
    type: [String],
    default: [],
    required: false
},
  url_pdf: { type: String, default: null },
  ecli: { type: String, default: null },
}, { _id: false });



const related_provisionsSchema = new Schema({
  article_name: { type: String },
  document_title: { type: String },
  shared_decision_count: { type: String }
}, { _id: false });


// Main Article schema
export const ArticleSchema = new Schema<IArticle>({
  id: { type: Number, required: true },                      
  hierarchy_element_id: { type: Number, required: true },                    
  article_number: { type: String, required: true },
  document_number: { type: String, required: true },                        
  anchor_id: { type: String, required: true },
  main_text: { type: String, required: true },
  gen_1:{type: String}, 
  gen_2:{type: String},
  gen_3:{type: String}, 
  created_at: { type: Date, required: true },
  cited_provision_count:{type:Number},
  related_provisions:{type:[related_provisionsSchema], default: []},
  decisions: { type: [DecisionForArticleSchema], default: [] }
}, {
  timestamps: true,
  versionKey: false,
  toJSON: { virtuals: true },
  toObject: { virtuals: true },
});

// Create compound unique index for article_number and document_number
ArticleSchema.index({ article_number: 1, document_number: 1 }, { unique: true });

const Article = mongoose.model<IArticle>('article', ArticleSchema);
export { Article };