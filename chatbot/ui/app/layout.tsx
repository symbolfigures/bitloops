import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Chat UI",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html>
      <head>
        <style>{`
          @font-face {
            font-family: 'CMSroman';
            src: url('/bitloops/chatbot/cmunrm.ttf');
          }
          @font-face {
            font-family: 'CMSbold';
            src: url('/bitloops/chatbot/cmunbx.ttf');
            font-weight: bold;
          }
          @font-face {
            font-family: 'CMSitalic';
            src: url('/bitloops/chatbot/cmunti.ttf');
            font-weight: italic;
          }
          @font-face {
            font-family: jsMath;
            src: url('/bitloops/chatbot/jsMath-cmsy10.ttf');
          }
          body {
            background-color: #000000;
            color: #ffffff;
            margin: 0;
            padding: 0;
			font-size: 18px;
          }
          a {
            color: #4da6ff;
          }
          button {
            background-color: #333333;
            color: #ffffff;
            border: 1px solid #666666;
            padding: 8px 16px;
			font-size: 18px;
            cursor: pointer;
            border-radius: 4px;
          }
          button:hover {
            background-color: #555555;
          }
          input, textarea {
            background-color: #1a1a1a;
            color: #ffffff;
            border: none;
            padding: 8px;
			font-size: 18px;
          }
        `}</style>
      </head>
      <body>
        {children}
      </body>
    </html>
  );
}