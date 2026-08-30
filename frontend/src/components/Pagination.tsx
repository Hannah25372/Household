import { LuChevronRight, LuChevronLeft } from "react-icons/lu";

type PaginationProps = {
  page: number;
  pageSize: number;
  total: number;
  onPageChange: (page: number) => void;
};

function Pagination({
  page,
  pageSize,
  total,
  onPageChange,
}: PaginationProps) {
  const totalPages = Math.ceil(total / pageSize);

  return (
    <div className="pagination">
      <button
        disabled={page === 1}
        onClick={() => onPageChange(page - 1)}
      ><LuChevronLeft/></button>
      <span>
        Page {page} of {totalPages}
      </span>
      <button
        disabled={page >= totalPages}
        onClick={() => onPageChange(page + 1)}
      ><LuChevronRight/></button>
    </div>
  );
}

export default Pagination;