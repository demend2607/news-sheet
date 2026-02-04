import Footer from "./Footer";
import Header from "./Header";

import "./layout.css";

export default function AppLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="layout">
      <Header />
      <main>{children}</main>
      <Footer />
    </div>
  );
}
