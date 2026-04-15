import Container from "@/shared/ui/Container";
import HeroNews from "@/components/hero-news/HeroNews";

import "./heroMain.css";
import PageWithSidebar from "@/components/side-bar/PageWithSideBar";
export default function HeroMain() {
  return (
    <PageWithSidebar>
      <HeroNews />
    </PageWithSidebar>
  );
}
