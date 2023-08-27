/*
  Warnings:

  - You are about to alter the column `barrier` on the `Effect` table. The data in that column could be lost. The data in that column will be cast from `Double` to `VarChar(191)`.

*/
-- AlterTable
ALTER TABLE `Effect` MODIFY `barrier` VARCHAR(191) NULL DEFAULT '0';
