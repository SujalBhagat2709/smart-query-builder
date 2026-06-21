class QueryParser:

    def parse(self, query):

        query = query.lower()

        if "all students" in query:

            if "cpi" in query and ">" in query:

                value = query.split(">")[-1].strip()

                return {
                    "table": "students",
                    "condition": f"cpi > {value}"
                }

            return {
                "table": "students"
            }

        elif "top 5 employees" in query:

            return {
                "table": "employees",
                "order_by": "salary",
                "limit": 5
            }

        elif "count students" in query:

            return {
                "table": "students",
                "count": True
            }

        return {
            "custom": True
        }