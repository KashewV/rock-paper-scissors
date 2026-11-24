from flask import Blueprint, request, render_template, redirect, flash

from app.stocks import fetch_stock_data

stocks_routes = Blueprint("stocks_routes", __name__)


@stocks_routes.route("/stocks/form")
def stocks_form():
    print("STOCKS FORM...")
    return render_template("stocks_form.html")


@stocks_routes.route("/stocks/dashboard", methods=["GET", "POST"])
def stocks_dashboard():
    print("STOCKS DASHBOARD...")

    if request.method == "POST":
        request_data = dict(request.form)  
    else:
        request_data = dict(request.args)  
    print("REQUEST DATA:", request_data)

    symbol = (request_data.get("symbol") or "NVDA").strip().upper()

    try:
        df = fetch_stock_data(symbol)

        
        if "adjusted_close" not in df.columns:
            raise ValueError(f"No data for symbol '{symbol}'")

        latest_close = f"${df.iloc[0]['adjusted_close']:,.2f}"
        latest_date = df.iloc[0]["timestamp"]
        data = df.to_dict("records")

        flash(f"Fetched market data for {symbol}!", "success")
        return render_template("stocks_dashboard.html",
            symbol=symbol,
            latest_close=latest_close,
            latest_date=latest_date,
            data=data
        )
    except Exception as err:
        print("OOPS:", err)
        flash(f"Market data error for '{symbol}'. Please check your symbol and try again!", "danger")
        return redirect("/stocks/form")