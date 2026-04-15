"use client";

import Link from "next/link";

import { Incident } from "@/entities/incidents/model/types";
import { getDate } from "@/shared/lib/hooks/utils";
export default function HeroCard({ incident }: { incident: Incident }) {
  const category = [incident.categories === "incidents" ? "Происшествия" : "Новости", "Хабаровск"];

  const date = getDate(incident.date);

  return (
    <article className="bg-white rounded-lg overflow-hidden shadow-sm">
      <div className="overflow-hidden">
        <img src={incident.images} alt={incident.title.slice(0, 40)} className="w-full h-full object-cover" />
      </div>
      <div className="p-6 space-y-4">
        {/* <span className="uppercase tracking-wide text-orange font-bold text-2xl">Lifestyle</span> */}
        <h4 className="font-semibold leading-snug text-xl">
          <Link href={`/incidents/${incident.id}`}>{incident.title}</Link>
        </h4>
        {/* <ul className="flex flex-wrap gap-4 text-sm text-gray-500">
          <li>
            <Link href="#" className="hover:text-gray-700">
              Admin
            </Link>
          </li>
          <li>
            {formateDate.day} {formateDate.month} {formateDate.year} {formateDate.localTime}
          </li>
          <li>12 Comments</li>
        </ul> */}
        <p className="text-gray-600 text-sm leading-relaxed">{incident.description}</p>
        <div className="flex gap-4 pt-4 border-t">
          <ul className="flex-1 flex flex-col items-center text-sm sm:flex-row sm:justify-between">
            <div className="flex gap-2">
              <li className="text-gray-400">🏷</li>
              {category.map((item, index) => (
                <li key={index}>
                  {item}
                  {index !== category.length - 1 && ","}
                </li>
              ))}
            </div>
            <li suppressHydrationWarning>
              {date.localTime}, {date.day} {date.month} {date.year} г.
            </li>
          </ul>
        </div>
      </div>
    </article>
  );
}
