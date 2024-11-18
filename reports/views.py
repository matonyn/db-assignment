from django.shortcuts import render
from django.db import connection

def index(request):
    results = []
    error = None

    if request.method == "POST":
        query = request.POST.get("query")

        try:
            with connection.cursor() as cursor:
                cursor.execute(query)

                # If the query returns data, fetch it
                if query.strip().lower().startswith("select"):
                    columns = [col[0] for col in cursor.description]
                    results = [dict(zip(columns, row)) for row in cursor.fetchall()]
                else:
                    # For non-SELECT commands, commit changes and show affected rows
                    connection.commit()
                    results = [{"Message": f"Query executed successfully. Rows affected: {cursor.rowcount}"}]

        except Exception as e:
            error = str(e)

    return render(request, "index.html", {"results": results, "error": error})
