import { Button } from '@mui/material';
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
            <StyledTableCell align='center'>Task</StyledTableCell>
            <StyledTableCell align='center'>Status</StyledTableCell>
            <StyledTableCell align='center'></StyledTableCell>
        </TableRow>
    </TableHead>
  );
};

const MyTableBody = ({tasks, handleDelete}) => {
  const rows = tasks.map((row, index) => {
    return (
      <StyledTableRow key={index}>
        <StyledTableCell component="th" scope="row" align='center'>{row.title}</StyledTableCell>
        <StyledTableCell align="center">{row.status}</StyledTableCell>
        <StyledTableCell align="center">
          <Button variant='contained' color='primary' size='small' onClick={() => handleDelete(index)}>Delete</Button>
        </StyledTableCell>
      </StyledTableRow>
    );
  });
  return <TableBody>{rows}</TableBody>
};

const TasksTable = ({tasks, handleDelete}) => {
    return (
      <Table sx={{ minWidth: 700 }} aria-label="customized table">
        <TableHeader />
        <MyTableBody tasks={tasks} handleDelete={handleDelete}/>
      </Table>
    );
}

export default TasksTable;