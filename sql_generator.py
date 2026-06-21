from query_parser import QueryParser


class SQLGenerator:

    def generate(self, parsed):

        if parsed.get("count"):

            return (
                f"SELECT COUNT(*) "
                f"FROM {parsed['table']};"
            )

        elif (
            "order_by" in parsed
        ):

            return (

                f"SELECT * "
                f"FROM {parsed['table']} "
                f"ORDER BY "
                f"{parsed['order_by']} DESC "
                f"LIMIT {parsed['limit']};"

            )

        elif (
            "condition" in parsed
        ):

            return (

                f"SELECT * "
                f"FROM {parsed['table']} "
                f"WHERE "
                f"{parsed['condition']};"

            )

        elif (
            "table" in parsed
        ):

            return (
                f"SELECT * "
                f"FROM {parsed['table']};"
            )

        return (
            "-- Unable to "
            "generate SQL"
        )


def save_sql(sql):

    with open(
        "query.sql",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(sql)


def main():

    print(
        "\n======================"
    )

    print(
        "SMART QUERY BUILDER"
    )

    print(
        "======================"
    )

    query = input(
        "\nEnter Query:\n"
    )

    parser = QueryParser()

    parsed = parser.parse(
        query
    )

    generator = SQLGenerator()

    sql = generator.generate(
        parsed
    )

    print(
        "\nGenerated SQL:\n"
    )

    print(sql)

    save_sql(sql)

    print(
        "\nSaved To:"
    )

    print(
        "query.sql"
    )


if __name__ == "__main__":

    main()