import { Pool } from 'pg';

export async function updateGet(
  pool: Pool,
): Promise<void> {
  const client = await pool.connect();
  try {
    const info = await client.query("select current_database() as db, current_user as usr");
    console.log("[updateGet] Target:", info.rows[0]);
    
    const updateQuery = `
      UPDATE public.article_contents ac
      SET
          gen_1 = LEFT(h2."label",75),
          gen_2 = LEFT(h3."label",75),
          gen_3 = LEFT(h4."label",75)
      FROM
          public.hierarchy_elements h1
          LEFT JOIN public.hierarchy_elements h2 ON h1.parent_id = h2.id
          LEFT JOIN public.hierarchy_elements h3 ON h2.parent_id = h3.id
          LEFT JOIN public.hierarchy_elements h4 ON h3.parent_id = h4.id
      WHERE
          ac.hierarchy_element_id = h1.id;
    `;
    
    const result = await client.query(updateQuery);
    console.log(`[updateGet] Success: Updated ${result.rowCount} rows in article_contents`);
    
  } catch (err) {
    console.error('[updateGet] Error:', err);
    throw err;
  } finally {
    client.release();
  }
}
