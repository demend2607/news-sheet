import { cn } from "../lib/hooks/utils";

export default function Loader() {
  return (
    <div className="space-y-4 ">
      <LoaderPiece className="h-4 w-[400px]" />
      <LoaderPiece className="h-4 w-[300px]" />
      <LoaderPiece className="h-4 w-[350px]" />
    </div>
  );
}

function LoaderPiece({ className }: { className?: string }) {
  return <div className={cn("animate-pulse h-4 w-[550px] rounded-md bg-white/5", className)} />;
}
