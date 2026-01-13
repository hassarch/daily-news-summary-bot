from app.formatter.base import BaseFormatter


class EmailFormatter(BaseFormatter):
    def format(self, data: dict) -> str:
        return f"""
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8" />
  <title>Daily News Digest</title>
</head>
<body style="margin:0; padding:0; background-color:#f4f6f8;">
  <table width="100%" cellpadding="0" cellspacing="0" style="background-color:#f4f6f8; padding:20px;">
    <tr>
      <td align="center">

        <!-- Main container -->
        <table width="600" cellpadding="0" cellspacing="0" style="background-color:#ffffff; border-radius:8px; overflow:hidden; font-family:Arial, sans-serif;">

          <!-- Header -->
          <tr>
            <td style="background-color:#1e90ff; padding:20px; color:#ffffff;">
              <h1 style="margin:0; font-size:22px;">📰 Daily News Digest</h1>
              <p style="margin:5px 0 0; font-size:14px;">Top stories you should know today</p>
            </td>
          </tr>

          <!-- Content -->
          <tr>
            <td style="padding:20px; color:#333333; font-size:14px; line-height:1.6;">
              {self._format_summary(data["summary"])}
            </td>
          </tr>

          <!-- Footer -->
          <tr>
            <td style="background-color:#f0f2f5; padding:15px; text-align:center; font-size:12px; color:#777777;">
              <p style="margin:0;">Generated automatically by Daily News Summarizer</p>
              <p style="margin:5px 0 0;">You are receiving this email because you subscribed.</p>
            </td>
          </tr>

        </table>

      </td>
    </tr>
  </table>
</body>
</html>
        """

    def _format_summary(self, summary_text: str) -> str:
        """
        Converts plain text summary into email-friendly HTML
        """
        lines = summary_text.split("\n")
        html = ""

        for line in lines:
            line = line.strip()
            if not line:
                html += "<br />"
            elif line.startswith("🔹"):
                html += f"<p style='margin:10px 0;'>🔹 {line[2:].strip()}</p>"
            elif line.startswith("🔗"):
                url = line.replace("🔗", "").strip()
                html += f"<p><a href='{url}' style='color:#1e90ff;'>Read full article →</a></p>"
            else:
                html += f"<p>{line}</p>"

        return html
