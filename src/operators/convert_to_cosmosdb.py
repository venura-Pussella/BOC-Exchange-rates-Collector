import uuid
def convert_df_to_cosmos_db_format(df):
    
    cosmos_db_documents = []
    for _, row in df.iterrows():
        rate_document = {
            "id": str(uuid.uuid4()),
            "timestamp": f"{row['Date']}T{row['Time']}Z",
            "code": row['Currency'],
            "currency_buying_rate": float(row['Currency_Buying_Rate']) if row['Currency_Buying_Rate'] else None,
            "currency_selling_rate": float(row['Currency_Selling_Rate']) if row['Currency_Selling_Rate'] else None,
            "travelers_cheques_buying_rate": float(row['Travelers Cheques/Drafts_Buying_Rate']) if row['Travelers Cheques/Drafts_Buying_Rate'] else None,
            "travelers_cheques_selling_rate": float(row['Travelers Cheques/Drafts_Selling_Rate']) if row['Travelers Cheques/Drafts_Selling_Rate'] else None,
            "telegraphic_transfers_PFCA_BFCA_buying_rate": float(row['Telegraphic/PFCA/BFCA Transfers_Buying_Rate']) if row['Telegraphic/PFCA/BFCA Transfers_Buying_Rate'] else None,
            "telegraphic_transfers_PFCA_BFCA_selling_rate": float(row['Telegraphic/PFCA/BFCA Transfers_Selling_Rate']) if row['Telegraphic/PFCA/BFCA Transfers_Selling_Rate'] else None,
            "bank": row['Bank'],
            "st_bank_code": row['ST BANK CODE']
        }
        cosmos_db_documents.append(rate_document)
    
    return cosmos_db_documents