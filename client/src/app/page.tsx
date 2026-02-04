import Image from "next/image";

import Carousel from "@/modules/home/carousel/ui/Carousel";
import AllBlog from "@/modules/home/hero-main/ui/HeroMain";

export default function Home() {
  return (
    <>
      <Carousel />
      <AllBlog />
    </>
  );
}
