import { styled } from '@mui/material/styles';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell, { tableCellClasses } from '@mui/material/TableCell';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';

const StyledTableCell = styled(TableCell)(({ theme }) => ({
  [`&.${tableCellClasses.head}`]: {
    backgroundColor: theme.palette.common.black,
    color: theme.palette.common.white,
  },
  [`&.${tableCellClasses.body}`]: {
    fontSize: 14,
  },
}));

const StyledTableRow = styled(TableRow)(({ theme }) => ({
  '&:nth-of-type(odd)': {
    backgroundColor: theme.palette.action.hover,
  },
  // hide last border
  '&:last-child td, &:last-child th': {
    border: 0,
  },
}));

const TableHeader = () => {
  return (
    <TableHead>
        <TableRow>
            <StyledTableCell>Task</StyledTableCell>
            <StyledTableCell align='right'>Status</StyledTableCell>
        </TableRow>
    </TableHead>
  );
};

const MyTableBody = () => {
  return (
    <TableBody>
        <StyledTableRow key={1}>
            <StyledTableCell component="th" scope="row">Task 1</StyledTableCell>
            <StyledTableCell align='right'>Done</StyledTableCell>
        </StyledTableRow>
        <StyledTableRow key={2}>
            <StyledTableCell component="th" scope="row">Task 2</StyledTableCell>
            <StyledTableCell align='right'>Done</StyledTableCell>
        </StyledTableRow>
        <StyledTableRow key={3}>
            <StyledTableCell component="th" scope="row">Task 3</StyledTableCell>
            <StyledTableCell align='right'>Not Done</StyledTableCell>
        </StyledTableRow>
    </TableBody>
  );
};

const TasksTable = () => {
    return (
      <Table sx={{ minWidth: 700 }} aria-label="customized table">
        <TableHeader />
        <MyTableBody />
      </Table>
    );
}

export default TasksTable;