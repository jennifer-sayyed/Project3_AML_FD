def generate_sar(
    customer,
    transactions,
    typology,
    source_docs
):

    return f"""
SAR Narrative

Customer: {customer}

Observed Activity:

{transactions}

Typology Match:

{typology}

Based on the detected pattern,
the activity is consistent with
money structuring indicators.

Recommended Action:

File STR for review.

Sources:

{source_docs}
"""