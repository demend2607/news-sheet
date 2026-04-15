// components/PageWithSidebar.tsx
import { ReactNode } from "react";
import Container from "@/shared/ui/Container";

interface PageWithSidebarProps {
  children: ReactNode;
}

export default function PageWithSidebar({ children }: PageWithSidebarProps) {
  return (
    <section id="hero__main">
      <Container>
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
          <div className="lg:col-span-8">{children}</div>
          <div className="lg:col-span-4">
            <aside className="space-y-6">
              <div className="bg-white p-4 rounded">
                <input type="text" placeholder="Type to search..." className="w-full border px-3 py-2 rounded" />
              </div>
              <div className="bg-white p-4 rounded">text</div>
              <div className="bg-white p-4 rounded">text</div>
              <div className="bg-white p-4 rounded">text</div>
            </aside>
          </div>
        </div>
      </Container>
    </section>
  );
}
