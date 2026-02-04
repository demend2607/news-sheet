import Container from "@/shared/ui/Container";

import "./heroMain.css";
export default function HeroMain() {
  return (
    <section id="hero__main">
      <Container>
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
          <div className="lg:col-span-8">
            <div className="space-y-6">
              <article className="bg-white rounded-lg overflow-hidden shadow-sm">
                <div className="overflow-hidden">
                  <img src="" alt="" className="w-full h-full object-cover" />
                </div>
                <div className="p-6 space-y-4">
                  <span className="uppercase tracking-wide text-orange font-bold text-2xl">Lifestyle</span>
                  <h4 className="font-semibold leading-snug text-xl">
                    <a href="/news">Best Template Website for HTML CSS</a>
                  </h4>
                  <ul className="flex flex-wrap gap-4 text-sm text-gray-500">
                    <li>
                      <a href="#" className="hover:text-gray-700">
                        Admin
                      </a>
                    </li>
                    <li>May 31, 2020</li>
                    <li>12 Comments</li>
                  </ul>
                  <p className="text-gray-600 text-sm leading-relaxed">
                    Stand Blog is a free HTML CSS template for your CMS theme. You can easily adapt or customize it for any kind of CMS or website
                    builder. You are allowed to use it for your business. You are NOT allowed to re-distribute the template ZIP file on any template
                    collection site for the download purpose.
                    <a href="" target="_parent" rel="nofollow" className="text-blue-600">
                      Contact TemplateMo
                    </a>
                    .
                  </p>
                  <div className="flex flex-col gap-4 pt-4 border-t sm:flex-row sm:justify-between">
                    <ul className="flex items-center gap-2 text-sm">
                      <li className="text-gray-400">🏷</li>
                      <li>
                        <a href="#">Beauty</a>,
                      </li>
                      <li>
                        <a href="#">Nature</a>
                      </li>
                    </ul>
                  </div>
                </div>
              </article>
            </div>
          </div>
          <div className="lg:col-span-4">
            <aside className="space-y-6">
              <div className="bg-white p-4 rounded">
                <input type="text" placeholder="Type to search..." className="w-full border px-3 py-2 rounded"></input>
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
