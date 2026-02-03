import Image from "next/image";

import Carousel from "@/modules/blog/carousel/ui/Carousel";
import AllBlog from "@/modules/blog/blog-posts/ui/AllBlog";

export default function Home() {
  return (
    <>
      <Carousel />
      <AllBlog />
    </>
  );
}
