
def sanctions_action(score):

    if score > 90:
        return """
        Potential sanctions match.
        Escalate immediately.
        Freeze transaction.
        Notify compliance unit.
        """

    return "Review required."
